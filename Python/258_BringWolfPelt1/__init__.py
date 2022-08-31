#SUBQUEST SONIN- FLORAN - QUEST 135_TempleExecutor
import sys
from net.sf.l2j import Config 
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

qn = "258_BringWolfPelt1"

WOLF_PELT = 702
#MONSTROS
MOB = [20934,20930,20935]
class Quest (JQuest) :

 def __init__(self,id,name,descr):
     JQuest.__init__(self,id,name,descr)
     self.questItemIds = [WOLF_PELT]

 def onAdvEvent (self,event,npc, player) :
    htmltext = event
    st = player.getQuestState(qn)
    if not st : return
    if event == "30001-03.htm" :
      st.set("cond","1")
      st.setState(State.STARTED)
      st.playSound("ItemSound.quest_accept")
    return htmltext

 def onTalk (self,npc,player):
   htmltext = "<html><body>Requisitos Inválidos.</body></html>"
   st = player.getQuestState(qn)
   if not st : return htmltext
   npcId = npc.getNpcId()
   id = st.getState()
   
   if id == State.CREATED :
     st.set("cond","0")
     
   if st.getInt("cond")==0 : 
     if player.getLevel() < 45 :
       htmltext = "30001-02.htm"
     else:
       htmltext = "noway.htm"
       st.exitQuest(1)   
   elif st.getQuestItemsCount(WOLF_PELT) > 14 :
     if player.getLevel() <= 44 :
       st.takeItems(WOLF_PELT,-1)
       st.giveItems(57,6000000)
       st.giveItems(951,4)
       st.giveItems(952,4)
       htmltext = "30001-06a.htm"
       st.exitQuest(1)
       st.playSound("ItemSound.quest_finish")
     if player.getLevel() > 44 :
       st.takeItems(WOLF_PELT,-1)
       st.giveItems(57,3000000)
       st.giveItems(951,1)
       st.giveItems(952,1)
       htmltext = "30001-06b.htm"
       st.exitQuest(1)
       st.playSound("ItemSound.quest_finish")  
   else :
     htmltext = "30001-05.htm"  
   return htmltext

 def onKill(self,npc,player,isPet):
   st = player.getQuestState(qn)
   if not st : return 
   if st.getState() != State.STARTED : return 
   
   count = st.getQuestItemsCount(WOLF_PELT)
   numItems, chance = divmod(100*Config.RATE_QUEST_DROP,100)
   if st.getRandom(100) <chance :
     numItems = numItems + 1
   if count+numItems>=15 :
     numItems = 15 - count
     if numItems != 0 :
       st.playSound("ItemSound.quest_middle")
       st.set("cond","2")
   else :
     st.playSound("ItemSound.quest_itemget")
   st.giveItems(WOLF_PELT,int(numItems))
   return

QUEST       = Quest(258,qn,"Mel e Abelhas")

QUEST.addStartNpc(31773)

QUEST.addTalkId(31773)

for npc in MOB :
   QUEST.addKillId(npc)