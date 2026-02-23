# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

## Monitoramento de Contexto para Jarlisson

# Objetivo: Alertar Jarlisson quando o contexto da nossa conversa atingir 50% da sua capacidade máxima.
# Esta é uma medida proativa para ajudar a prevenir erros como 'request entity too large' (413).

# Nota de Implementação: Atualmente, não há um comando ou ferramenta direta disponível para que eu possa consultar o uso de tokens/contexto em tempo real.
# Assim que o OpenClaw proporcionar um mecanismo interno ou API para essa funcionalidade, o placeholder abaixo será atualizado para monitorar e enviar o alerta proativamente.

# PSEUDO-CÓDIGO (para futura implementação):
# SE (uso_do_contexto_atual() >= 0.50 * capacidade_maxima_do_contexto()) ENTÃO
#    message action=send to=Jarlisson message="ALERTA: Meu contexto de conversa atingiu 50% de uso. Considere a sumarização em breve."
# FIM SE