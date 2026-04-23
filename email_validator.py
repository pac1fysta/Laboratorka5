import re

def is_valid_email(email: str) -> bool:
    """
    Проверяет, является ли строка корректным email-адресом.
    """
    if not isinstance(email, str):
        return False
    
    # Более строгое регулярное выражение
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9][a-zA-Z0-9.-]*\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        # Проверяем, что нет точек подряд и нет точки сразу после @
        local_part, domain_part = email.split('@')
        
        # Локальная часть не должна начинаться или заканчиваться точкой
        if local_part.startswith('.') or local_part.endswith('.'):
            return False
        
        # Доменная часть не должна иметь две точки подряд
        if '..' in domain_part:
            return False
        
        # Доменная часть не должна начинаться или заканчиваться точкой
        if domain_part.startswith('.') or domain_part.endswith('.'):
            return False
        
        return True
    
    return False