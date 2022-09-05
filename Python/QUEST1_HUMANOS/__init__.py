# Quest - 1 Humanos 
import sys
from net.sf.l2j import Config
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest
qn = "101_SwordOfSolidarity"


#NPCS
ARTURO = 30598
COLLIN = 30311
#ITENS
ROIENS_LETTER = 796
HOWTOGO_RUINS = 937
BROKEN_SWORD_HANDLE = 739
BROKEN_BLADE_BOTTOM = 740
BROKEN_BLADE_TOP = 741
ALLTRANS_NOTE = 742
SOULSHOT_FOR_BEGINNERS = 5789

class Quest (JQuest) :

 def __init__(self,id,name,descr):
     JQuest.__init__(self,id,name,descr)
     self.questItemIds = [ALLTRANS_NOTE, HOWTOGO_RUINS, BROKEN_BLADE_TOP, BROKEN_BLADE_BOTTOM, ROIENS_LETTER, BROKEN_SWORD_HANDLE]

 def onAdvEvent (self,event,npc, player) :
    htmltext = event
    st = player.getQuestState(qn)
    if not st : return
    if event == "30008-01.htm" :
        st.set("cond","1")
        st.setState(State.STARTED)
        st.playSound("ItemSound.quest_accept")
        st.giveItems(ROIENS_LETTER,1)
    elif event == "talknpc2.htm" :
        st.set("cond","2")
        st.playSound("ItemSound.quest_middle")
        st.takeItems(ROIENS_LETTER,st.getQuestItemsCount(ROIENS_LETTER))
        st.giveItems(HOWTOGO_RUINS,1)
        st.addRadar(-113490,235526,-3646)
        
        #FINISH QUEST
    elif event == "end.htm" :
        st.takeItems(BROKEN_SWORD_HANDLE,-1)
        st.giveItems(57,3000000)
        st.giveItems(725,12)
        st.giveItems(726,12)
        st.addExpAndSp(45747,2171)
        st.unset("cond")
        st.exitQuest(False)
        st.playSound("ItemSound.quest_finish")
    return htmltext


 def onTalk (self,npc,player) :
   npcId = npc.getNpcId()
   htmltext = "<html><body><br><br><br><center>Sem os Requisitos.</center></body></html>" 
   st = player.getQuestState(qn)
   if not st: return htmltext
   id = st.getState()
   if id == State.COMPLETED : 
        htmltext = "finish.htm"
   elif npcId == ARTURO and id == State.CREATED :
      #protecao de racas
      if player.getRace().ordinal() != 0 :
        htmltext = "nohuman.htm"
        #Level que inicia
      elif player.getLevel() >= 9 :
        htmltext = "start.htm"
        return htmltext
      else:
        htmltext = "noway.htm"
        st.exitQuest(1)
       #STATUS DE QUEST INICIADA
   elif id == State.STARTED: 
       if npcId == ARTURO and st.getInt("cond")==1 and (st.getQuestItemsCount(ROIENS_LETTER)==1) :
            htmltext = "findnpc.htm"
       elif npcId == ARTURO and st.getInt("cond")>=2 and st.getQuestItemsCount(ROIENS_LETTER)==0 and st.getQuestItemsCount(ALLTRANS_NOTE)==0 :
            if st.getQuestItemsCount(BROKEN_SWORD_HANDLE) > 0 :
              htmltext = "finish-end.htm"
            if st.getQuestItemsCount(HOWTOGO_RUINS) == 1 :
              htmltext = "semitem.htm"
           
            
            
       #OBELISCO DA VITORIA - COLLIN WINDAWOOD
       elif npcId == COLLIN and st.getInt("cond")==1 and (st.getQuestItemsCount(ROIENS_LETTER)>0) :
            htmltext = "talknpc1.htm"
       elif npcId == COLLIN and st.getInt("cond")>=2 and st.getQuestItemsCount(ROIENS_LETTER)==0 and st.getQuestItemsCount(HOWTOGO_RUINS)>0 :
            if (st.getQuestItemsCount(BROKEN_BLADE_TOP) + st.getQuestItemsCount(BROKEN_BLADE_BOTTOM)) == 1 :
              htmltext = "apenas1.htm"
            if (st.getQuestItemsCount(BROKEN_BLADE_TOP) + st.getQuestItemsCount(BROKEN_BLADE_BOTTOM)) == 0 :
              htmltext = "semitem.htm"
       #deCollin para Villa
       elif npcId == COLLIN and st.getInt("cond")==4 and st.getQuestItemsCount(ALLTRANS_NOTE) :
            htmltext = "paraarturo.htm"
            st.set("cond","5")
            st.playSound("ItemSound.quest_middle")
            st.takeItems(ALLTRANS_NOTE,st.getQuestItemsCount(ALLTRANS_NOTE))
            st.giveItems(BROKEN_SWORD_HANDLE,1)
            player.teleToLocation(-84332,243831,-3730)
       elif npcId == COLLIN and id == State.COMPLETED :
            htmltext = "findarturo.htm"   
 
       #Rammus
       elif npcId == 30667 and st.getInt("cond")==3 :
            htmltext = "findlionel.htm"
            st.addRadar(-113446,235578,-3646)            
       elif npcId == 30667 and id == State.COMPLETED :
            htmltext = "findarturo.htm"   
        #LIONEL PARA COLLIN
       elif npcId == 30408 and st.getInt("cond")>=2 and st.getQuestItemsCount(ROIENS_LETTER)==0 and st.getQuestItemsCount(HOWTOGO_RUINS)>0 :
            if st.getQuestItemsCount(BROKEN_BLADE_TOP) and st.getQuestItemsCount(BROKEN_BLADE_BOTTOM) :
              htmltext = "finishitem.htm"
              st.set("cond","4")
              st.playSound("ItemSound.quest_middle")
              st.takeItems(HOWTOGO_RUINS,st.getQuestItemsCount(HOWTOGO_RUINS))
              st.takeItems(BROKEN_BLADE_TOP,st.getQuestItemsCount(BROKEN_BLADE_TOP))
              st.takeItems(BROKEN_BLADE_BOTTOM,st.getQuestItemsCount(BROKEN_BLADE_BOTTOM))
              st.giveItems(ALLTRANS_NOTE,1)
              st.addRadar(-100648,237561,-3574)
       elif npcId == 30408 and st.getInt("cond")==4 :
            htmltext = "finishitem.htm"
            st.addRadar(-113446,235578,-3646)                     
                
   return htmltext




 def onKill(self,npc,player,isPet):
   st = player.getQuestState(qn)
   if not st: return   
   if st.getState() == State.STARTED :
       npcId = npc.getNpcId()
       if npcId in [20361,20362] :
          if st.getQuestItemsCount(HOWTOGO_RUINS) :
             if st.getQuestItemsCount(BROKEN_BLADE_TOP) == 0 :
                if st.getRandom(100):
                   st.giveItems(BROKEN_BLADE_TOP,1)
             elif st.getQuestItemsCount(BROKEN_BLADE_BOTTOM) == 0 :
                if st.getRandom(100) :
                   st.giveItems(BROKEN_BLADE_BOTTOM,1)
          if st.getQuestItemsCount(BROKEN_BLADE_TOP) and st.getQuestItemsCount(BROKEN_BLADE_BOTTOM) :
             st.set("cond","3")
             st.playSound("ItemSound.quest_middle")
          else :
             st.playSound("ItemSound.quest_itemget")
   return

QUEST       = Quest(101,qn,"1º Cidade dos Humanos")



#NPC QUE INICIA A QUEST
QUEST.addStartNpc(ARTURO)
QUEST.addTalkId(ARTURO)
#OUTROS NPCS
QUEST.addTalkId(30667)
QUEST.addTalkId(30408)
QUEST.addTalkId(COLLIN)
#MOBS PARA PMATAR
QUEST.addKillId(20361)
QUEST.addKillId(20362)
