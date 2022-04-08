#============================================================================================================================================
#                                                           NPC PORTAL PARA HUMANOS, ELFOS E DARK ELFOS... 
#============================================================================================================================================
#IMPORTS DO CORE.JAR
import sys
from net.sf.l2j.gameserver.datatables import DoorTable
from net.sf.l2j.gameserver.model.actor.instance import L2PcInstance
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

#NOME DA QUEST NO ARQUIVO SCRIPTS.confg
qn = "12369_TeleportNewbies"


#====================================================================================================
#                   TALKING INSTALND    -   ELVEN VILLAGE   -   DARK ELVEN VILLAGE                  =
#====================================================================================================
#                                      |                    |                         |             =  
#                                                                                                   =
#                                                                                                   =
#====================================================================================================



#LISTA DE NPCS
NPCS=[32034,32035,32036,32037,32039,32040,1230]

# Main Quest Code
class Quest (JQuest):
  def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)


  #Essa funcao faz com que o personagem ao clicar 2 vezes, antes de abrir o chat, o FIRST TALK.
  def onFirstTalk (self,npc,player):
    npcId = npc.getNpcId()
    
    #Teleportador  de Retorno para  Talking Island
    if npcId == 1231 :
       player.teleToLocation(-85536,241480,-3730)
       
    #elif npcId == 32040 :
       #player.teleToLocation(36640,-51218,718)
    return ""

    #Funcao responsavel por abrir o chat e fazer referencias.
    #normalmente chamado por uma html como o exemplo abaixo
    #" action="bypass -h npc_%objectId%_Quest 12369_TeleportNewbies" 
  def onTalk (self,npc,player):
    st = player.getQuestState(qn)
    npcId = npc.getNpcId()
    htmltext = None

    # HTML Sem Itens 
    # Se conter ou NAO na mochila do personagem na Aba Quests (QuestItems) 
    #Referencia dos "IDS Dos ITENS" feita no Banco de dados na tabela ETCITENS.
    if npcId == 1230 and st.getQuestItemsCount(1512)== 0 and st.getQuestItemsCount(1513)== 0:   
         htmltext = "1230-00.htm"
         
         
#====================================
#======       ESTRUTURA 1  ==========
#TALKING ISLAND - 1512
#ELVEN VILLAGE - 1513
#DARK ELVEN VILLAGE
#====================================
#=================================================================================================== 1512 LIVRO 1 - Paginas Talking
    elif npcId == 1230 :
        #INICIAL DAS RACAS COMECANDO PELOS HUMANOS 
#===================================================================================================        
           #item 1
         if st.getQuestItemsCount(1512) == 1 and st.getQuestItemsCount(1514)== 1 :
           htmltext = "1230-01.htm"    
           #item 2                     
         if st.getQuestItemsCount(1512) == 1 and st.getQuestItemsCount(1515)== 1 :
           htmltext = "1230-1.htm"     
           #item 3                     
         if st.getQuestItemsCount(1512) == 1 and st.getQuestItemsCount(1516)== 1 :
           htmltext = "1230-02.htm"
#=================================================================================================== QUEST DE CLASSES
           # QUEST WARRIOR HUMANOS  401_PathToWarrior
         if st.getQuestItemsCount(1512) == 1 and st.getQuestItemsCount(4906) and st.getQuestItemsCount(1517) :
           htmltext = "1230-warrior.htm"      
    #===========================================================================
           # QUEST ROGUE HUMANOS   403_PathToRogue
         if st.getQuestItemsCount(1512) == 1 and st.getQuestItemsCount(1180)==1 and st.getQuestItemsCount(1185)==1 :
           htmltext = "1230-rogue.htm"            
    #===========================================================================
           # QUEST Knight HUMANOS  402_PathToKnight
         if st.getQuestItemsCount(1512) == 1 and st.getQuestItemsCount(1271) == 1 and not st.getQuestItemsCount(1168):
           htmltext = "1230-knight.htm" 
         if st.getQuestItemsCount(1512) == 1 and st.getQuestItemsCount(1168) == 1 and st.getQuestItemsCount(1170)== 1 and st.getQuestItemsCount(1172)== 1  and st.getQuestItemsCount(1174) == 1 and st.getQuestItemsCount(1176)== 1 and st.getQuestItemsCount(1178)== 1 :
           htmltext = "1230-knightmobs.htm"            
#=================================================================================================== FIM DA QUEST DE CLASSE
 
#=========================================================================== 1512 LIVRO 1- Gludin -> Gludio
           #item 2 //Quest Gludin - DRAGON FANGS_38 - QUEST CLAN LANGk
         if st.getQuestItemsCount(1512)== 1  and st.getQuestItemsCount(1517) == 1 and st.getQuestItemsCount(689) == 1:
           htmltext = "1230-3.htm"
           #TELEPORT ROHMER DIRETO PRA GLUDIO 
         if st.getQuestItemsCount(1512)== 1  and st.getQuestItemsCount(1517) == 1 and st.getQuestItemsCount(689)  == 1 and st.getQuestItemsCount(7176) == 1 :
           htmltext = "1230-3b.htm"
           #TELEPORT IRIS DIRETO PRA GLUDIN 
         if st.getQuestItemsCount(1512)== 1  and st.getQuestItemsCount(1517) == 1 and st.getQuestItemsCount(689)  == 1 and st.getQuestItemsCount(7177)  == 1 :
           htmltext = "1230-3ba.htm"
           #BOSS
         if st.getQuestItemsCount(1512)== 1  and st.getQuestItemsCount(1517) == 1 and st.getQuestItemsCount(692)  == 1 :
           htmltext = "1230-3a.htm"
# ==============================================================================  1512 LIVRO 1- Gludio -> Dion
           #item 3//Quest Gludin ACTS OF EVIL_171
         if st.getQuestItemsCount(1512)== 1 and st.getQuestItemsCount(1518)== 1 :
           htmltext = "1230-04.htm"
         if st.getQuestItemsCount(1512)== 1 and st.getQuestItemsCount(1518)== 1 and st.getQuestItemsCount(693) == 1:
           htmltext = "1230-04a.htm"         
         if st.getQuestItemsCount(1512)== 1 and st.getQuestItemsCount(1518)== 1 and st.getQuestItemsCount(4240) == 1 and st.getQuestItemsCount(693) == 1:
           htmltext = "1230-04b.htm"           
# ==============================================================================             
           #Go to Dion // Level 40 // Temple executor_135/Missionary_
         if st.getQuestItemsCount(1512)== 1  and st.getQuestItemsCount(1519)== 1 :
           htmltext = "1230-final40.htm"
         if st.getQuestItemsCount(1512)== 1  and st.getQuestItemsCount(1519)== 1 and st.getQuestItemsCount(720) == 1:
           htmltext = "final40-dion1.htm"
           
         if st.getQuestItemsCount(689) == 1 and st.getQuestItemsCount(691) == 1 and st.getQuestItemsCount(691) == 1:
           htmltext = "portogiran.htm"           
#================================================ FINAL ESTRUTURA - Level 1 Ate Level 40 , as 3 Vilas. GLUDIN, GLUDIO E DION.                 
    st.exitQuest(1)
    return htmltext

# Quest class and state definition (Busca na QuestList em Scripts.cfg dir/data/script.cfg
QUEST       = Quest(12369, qn, "Teleports")

# Quest NPC starter initialization
for npc in NPCS :
    QUEST.addStartNpc(npc)
    QUEST.addTalkId(npc)
QUEST.addFirstTalkId(1231)
QUEST.addFirstTalkId(1237)