
from models.activateHelper import activateHelper


datab = activateHelper()

act = datab.getActivate()
print(act['active_text'])
