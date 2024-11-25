import shodan
import requests
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SHODAN = os.getenv('SHODAN_API_KEY')

class CyberSecurity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api = shodan.Shodan(SHODAN)

    @commands.command(name='scan_ip')
    async def scan_ip(self, ctx, ip_address):
        """Escanea una dirección IP usando Shodan."""
        if not ip_address:
            await ctx.send("Por favor, proporciona una dirección IP.")
            return

        try:
            result = self.api.host(ip_address)
            response = f"Información de {ip_address}:\n"
            response += f"Organización: {result.get('org', 'N/A')}\n"
            response += f"Nombre de host: {result.get('hostnames', ['N/A'])[0]}\n"
            response += f"Servicios: {', '.join(result.get('services', ['N/A']))}\n"
            response += f"Puertos: {', '.join(map(str, result.get('ports', [])))}"
            await ctx.send(response)
        except shodan.APIError as e:
            await ctx.send(f"Error de Shodan: {e}")
        except Exception as e:
            await ctx.send(f"Error al escanear la IP: {e}")

    @commands.command(name='webCHK')
    async def webCHK(self, ctx, domain_or_ip):
        """Obtiene un análisis de seguridad detallado desde web-check.xyz y filtra resultados."""
        if not domain_or_ip:
            await ctx.send("Por favor, proporciona un dominio o una dirección IP.")
            return

        try:
            # Llamada a la API de web-check.xyz
            url = f"https://web-check.xyz/check?domain={domain_or_ip}"
            response = requests.get(url)

            # Verifica si la solicitud fue exitosa
            if response.status_code != 200:
                await ctx.send(f"Error: No se pudo obtener información de web-check.xyz. Código de estado: {response.status_code}")
                return

            # Verifica si la respuesta tiene contenido antes de procesarlo como JSON
            if not response.text:
                await ctx.send("Error: La respuesta está vacía.")
                return

            try:
                data = response.json()  # Intenta procesar el JSON
            except ValueError as e:
                await ctx.send(f"Error al procesar la respuesta JSON: {e}")
                return

            # Filtrar y estructurar los resultados
            server_location = data.get("Server Location", "N/A")
            ssl_info = data.get("SSL Certificate", "N/A")
            dns_records = data.get("DNS Records", "N/A")
            open_ports = data.get("Open Ports", "N/A")
            server_info = data.get("Server Info", "N/A")
            firewall_detection = data.get("Firewall Detection", "N/A")
            tls_cipher_suites = data.get("TLS Cipher Suites", "N/A")

            # Crear la respuesta con los datos filtrados
            response_message = f"**Análisis de seguridad para {domain_or_ip}:**\n\n"
            
            # Ubicación del servidor
            if server_location != "N/A":
                response_message += f"**Ubicación del Servidor:**\n"
                response_message += f"- Ciudad: {server_location.get('City', 'N/A')}\n"
                response_message += f"- País: {server_location.get('Country', 'N/A')}\n"
                response_message += f"- Zona Horaria: {server_location.get('Timezone', 'N/A')}\n\n"

            # Información SSL
            if ssl_info != "N/A":
                response_message += f"**Certificado SSL:**\n"
                response_message += f"- Emisor: {ssl_info.get('Issuer', 'N/A')}\n"
                response_message += f"- Expira: {ssl_info.get('Expires', 'N/A')}\n"
                response_message += f"- Fingerprint: {ssl_info.get('Fingerprint', 'N/A')}\n\n"

            # Registros DNS
            if dns_records != "N/A":
                response_message += f"**Registros DNS:**\n"
                for record_type, record_value in dns_records.items():
                    response_message += f"- {record_type}: {record_value}\n"
                response_message += "\n"

            # Puertos abiertos
            if open_ports != "N/A":
                response_message += f"**Puertos Abiertos:** {', '.join(map(str, open_ports))}\n\n"

            # Información del servidor
            if server_info != "N/A":
                response_message += f"**Información del Servidor:**\n"
                response_message += f"- Proveedor: {server_info.get('Provider', 'N/A')}\n"
                response_message += f"- Tipo de Servidor: {server_info.get('Type', 'N/A')}\n\n"

            # Detección de firewall
            if firewall_detection != "N/A":
                response_message += f"**Detección de Firewall:** {firewall_detection}\n\n"

            # Suites de cifrado TLS
            if tls_cipher_suites != "N/A":
                response_message += f"**Suites de Cifrado TLS:** {', '.join(tls_cipher_suites)}\n\n"

            # Enviar la respuesta final al canal de Discord
            await ctx.send(response_message)

        except Exception as e:
            await ctx.send(f"Error al obtener la información: {e}")

async def setup(bot):
    await bot.add_cog(CyberSecurity(bot))
