def check_admin_role(member, admin_role_id):
    """Verifica si un miembro tiene el rol de administrador."""
    return any(role.id == admin_role_id for role in member.roles)
