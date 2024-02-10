import logging
import json

# Configuración de logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Función para generar un registro de log en formato JSON
def generate_log_message(message, log_level=logging.INFO):
    log_data = {
        'timestamp': logging.Formatter().format(logging.LogRecord(None, None, '', 0, log_level, message, None)),
        'level': logging.getLevelName(log_level),
        'message': message
    }
    return json.dumps(log_data)

# Ejemplo de uso
if __name__ == "__main__":
    # Generar logs de diferentes niveles
    logging.debug(generate_log_message("This is a debug message"))
    logging.info(generate_log_message("This is an info message"))
    logging.warning(generate_log_message("This is a warning message"))
    logging.error(generate_log_message("This is an error message"))
    logging.critical(generate_log_message("This is a critical message"))

