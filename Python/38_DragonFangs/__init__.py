#DRAGON FANGS EXPURGO

import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

qn = "38_DragonFangs"

#Quest items
FEATHER_ORNAMENT,TOOTH_OF_TOTEM,TOOTH_OF_DRAGON,LETTER_OF_CRETA,LETTER_OF_ROHMER = range(7173,7178)

#Drop info: cond,item,max,chance
DROPLIST={20198:[1,FEATHER_ORNAMENT,20,100],
          20160:[1,FEATHER_ORNAMENT,20,100],
          20201:[1,FEATHER_ORNAMENT,20,100],
          20202:[1,FEATHER_ORNAMENT,20,100],
          20200:[1,FEATHER_ORNAMENT,20,100],
          20171:[1,FEATHER_ORNAMENT,20,100],
          20026:[6,TOOTH_OF_DRAGON,10,100],
          20457:[6,TOOTH_OF_DRAGON,10,100]}
#Rewards: item,adena
#METODOZINHO TOP
#REWARDS=[[189,1254804],[8915,1657048]]
#NPC
LEVIAN = 30037
BELKIS=32143
CRETA=30609
SYLVAIN=30070
ROHMER=30344

PEITO = 1146
CALCA = 1147
LUVA = 1119
BOTA = 1129

class Quest (JQuest) :

 def __init__(self,id,name,descr):
     JQuest.__init__(self,id,name,descr)
     self.questItemIds = 7173,7174,7175,7176,7177,7178,692

 def onEvent (self,event,st) :
    htmltext = event
    if event == "30386-02.htm" : #START QUEST
       st.set("cond","1")
       st.setState(State.STARTED)
       st.playSound("ItemSound.quest_accept")
       
    elif event == "30386-04.htm" : #GO TO DION SYLVAIN
       st.set("cond","3")
       st.takeItems(FEATHER_ORNAMENT,-1)
       st.giveItems(TOOTH_OF_TOTEM,1)
       st.playSound("ItemSound.quest_middle")
       st.getPlayer().teleToLocation(15811,142840,-2707)
       
    elif event == "30034-02a.htm" and st.getQuestItemsCount(TOOTH_OF_TOTEM) : #SYLVAIN EM DION PARA ROHMER EM GLUDIO
       htmltext = "30034-02.htm"
       st.set("cond","4")
       st.takeItems(TOOTH_OF_TOTEM,1)
       st.giveItems(LETTER_OF_CRETA,1)
       st.playSound("ItemSound.quest_middle")
       
    elif event == "30344-02a.htm" and st.getQuestItemsCount(LETTER_OF_CRETA) : # DE ROMER PARA SYLVAIN
       htmltext = "30344-02.htm"
       st.set("cond","5")
       st.takeItems(LETTER_OF_CRETA,1)
       st.giveItems(LETTER_OF_ROHMER,1)
       st.playSound("ItemSound.quest_middle")
       
       
    elif event == "30034-04a.htm" and st.getQuestItemsCount(LETTER_OF_ROHMER) : #DE SYLVAIN PARA 
       st.takeItems(LETTER_OF_ROHMER,1)
       htmltext = "30034-04.htm"
       st.set("cond","6")
       st.playSound("ItemSound.quest_middle")
       
       
       
    elif event == "30034-06a.htm" and st.getQuestItemsCount(TOOTH_OF_DRAGON) == 10 : #Concluindo Quest BELKIS
       htmltext = "30034-06.htm"
       st.unset("cond")
       st.takeItems(TOOTH_OF_DRAGON,-1)
       st.playSound("ItemSound.quest_finish")
       #item,adena=REWARDS[st.getRandom(len(REWARDS))]#VAMO BRINCAR
       #st.giveItems(item,qty)
       st.giveItems(189,1)       
       st.giveItems(8915,1)       
       st.giveItems(140,1)
       st.giveItems(437,1)
       st.giveItems(470,1)
       st.giveItems(2450,1)       
       st.addExpAndSp(33000,0)
       st.exitQuest(False)
              
    elif event == "Desespero" and st.getQuestItemsCount(LETTER_OF_ROHMER) : #START COND 6
       st.takeItems(LETTER_OF_ROHMER,1)
       htmltext = "30034-04.htm"
       st.set("cond","6")
       st.playSound("ItemSound.quest_middle")
       st.getPlayer().teleToLocation(-55500,107261,-3711)
       
    elif event == "Agonia" and st.getQuestItemsCount(LETTER_OF_ROHMER) : #START COND 6 
       st.takeItems(LETTER_OF_ROHMER,1)
       htmltext = "30034-04.htm"
       st.set("cond","6")
       st.playSound("ItemSound.quest_middle")
       st.getPlayer().teleToLocation(-19678,138380,-3898) 
    elif event == "Expurgar" : 
       st.getPlayer().teleToLocation(49600,149662,-2433)    
    elif event == "Gludio" : 
       st.getPlayer().teleToLocation(-12187,122557,-3062)            
    elif event == "Dion" : 
       st.getPlayer().teleToLocation(15811,142840,-2707)     
    return htmltext


 def onTalk (self,npc,player):
   htmltext = "<html><body>Nada por aqui.</body></html>"
   st = player.getQuestState(qn)
   if not st : return htmltext
   npcId = npc.getNpcId()
   id = st.getState()
   cond=st.getInt("cond")
   if id == State.COMPLETED :
      htmltext = "finish.htm"
      
      
   elif npcId == LEVIAN :
      if cond == 0 :
        if player.getLevel() >= 20 and player.getClassId().getId() == 0x0f and 0x1d and 0x2a:
           htmltext = "30386-01.htm"
        else :
           st.exitQuest(1)
           htmltext = "30386-01a.htm"
      elif cond == 1 :
        htmltext = "30386-02a.htm"      
       
   elif npcId == CRETA :       
      if cond >= 1 and st.getQuestItemsCount(FEATHER_ORNAMENT) == 20 :
        htmltext = "30386-03.htm"
      elif cond >= 1 and not st.getQuestItemsCount(FEATHER_ORNAMENT) == 20 :
        htmltext = "30386-03a.htm"               
      elif cond == 4 : #PROCURE POR ROHMER
        htmltext = "30034-02b.htm"
        
   elif npcId == SYLVAIN :
      if cond == 3 : #DION SYLVAIN MANDA PARA ROHMER
        htmltext = "30034-01.htm"
      elif cond == 4 : #PROCURE POR ROHMER
        htmltext = "30034-02b.htm"        
      elif cond == 5 : # DE ROMER PARA SYLVAIN
        htmltext = "30034-03.htm"        
      elif cond == 6 : # RUINAS DA AGONIA OU DESESPERO
        htmltext = "30034-05a.htm"           
        
   elif npcId == ROHMER :
      if cond == 4 :
         htmltext = "30344-01.htm"
      elif cond == 5 : # PARA SYLVAIN
         htmltext = "30344-03.htm"
      elif cond > 5 : # Protecao
         htmltext = "30344-03a.htm"         


   elif npcId == BELKIS :
      if cond == 5 and st.getQuestItemsCount(LETTER_OF_ROHMER) >= 1 :
        htmltext = "30034-05a.htm"
      elif cond == 5 and not st.getQuestItemsCount(LETTER_OF_ROHMER) >= 1 :
        htmltext = "30386-05b.htm"  
      elif cond == 7 :
        htmltext = "30034-05.htm"        
            
   return htmltext

 def onKill(self,npc,player,isPet):
   st = player.getQuestState(qn)
   if not st : return
   if st.getState() != State.STARTED : return
   cond = st.getInt("cond")
   cond,item,max,chance=DROPLIST[npc.getNpcId()]
   count=st.getQuestItemsCount(item)
   if st.getInt("cond") == cond and count < max and st.getRandom(100) < chance :
      st.giveItems(item,1)
      if count == max-1 :
         st.playSound("ItemSound.quest_middle")
         st.set("cond",str(cond+1))
      else :
         st.playSound("ItemSound.quest_itemget")
   return

QUEST       = Quest(38,qn,"Expurgo I")

QUEST.addStartNpc(LEVIAN)

QUEST.addTalkId(LEVIAN)
QUEST.addTalkId(BELKIS)
QUEST.addTalkId(CRETA)
QUEST.addTalkId(SYLVAIN)
QUEST.addTalkId(ROHMER)

for mob in DROPLIST.keys():
    QUEST.addKillId(mob)