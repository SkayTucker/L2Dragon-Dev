# TUTORIAL l2DRAGON PTBR
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest
from net.sf.l2j.gameserver.network.serverpackets import PlaySound
from net.sf.l2j import Config

qn = "999_T1Tutorial"
qnTutorial = "255_Tutorial"

RECOMMENDATION_01 = 1067
RECOMMENDATION_02 = 1068
LEAF_OF_MOTHERTREE = 1069
BLOOD_OF_JUNDIN = 1070
SOULSHOT_NOVICE = 5789
SPIRITSHOT_NOVICE = 5790
BLUE_GEM=6353
TOKEN = 8542
SCROLL= 8594
DIPLOMA = 9881

#event:    [htmlfile,radarX,radarY,radarZ,item,classId1,gift1,count1                         ,classId2,gift2,count2]
EVENTS={
#HUMANOS 
"30008_02":["30008-03.htm",     0,      0,    0,RECOMMENDATION_01 ,0x00,SOULSHOT_NOVICE  ,200,0x00,              0,  0],
"30008_04":["30008-04.htm",-84058, 243239,-3730,                 0,0x00,                0,  0,   0,              0,  0],
"30017_02":["30017-03.htm",     0,      0,    0,RECOMMENDATION_02 ,0x0a,SPIRITSHOT_NOVICE,100,0x00,              0,  0],
"30017_04":["30017-04.htm",-84058, 243239,-3730,                 0,0x0a,                0,  0,0x00,              0,  0],
#ELFOS
"30370_02":["30370-03.htm",     0,      0,    0,LEAF_OF_MOTHERTREE,0x19,SPIRITSHOT_NOVICE,100,0x12,SOULSHOT_NOVICE,200],
"30370_04":["30370-04.htm", 45491,  48359,-3086,                 0,0x19,                0,  0,0x12,              0,  0],
#DELFOS
"30129_02":["30129-03.htm",     0,      0,    0,BLOOD_OF_JUNDIN   ,0x26,SPIRITSHOT_NOVICE,100,0x1f,SOULSHOT_NOVICE,200],
"30129_04":["30129-04.htm", 12116,  16666,-4610,                 0,0x26,                0,  0,0x1f,              0,  0],
#KAMEL
"32133_02":["32133-03.htm",-119692, 44504,  380,DIPLOMA               ,0x7b,SOULSHOT_NOVICE  ,200,0x7c,SOULSHOT_NOVICE,200]
}

# npcId:[raceId,[htmlfiles],npcTyp,item]
TALKS={
#HUMANOS
30017:[0,["30017-01.htm","30017-02.htm","30017-04.htm"],0,0],
30008:[0,["30008-01.htm","30008-02.htm","30008-04.htm"],0,0],
30009:[0,["tutolutador-1.htm","tutolutador-2.htm",0,"30009-04.htm",],1,RECOMMENDATION_01],
30011:[0,["tutolutador-1.htm","30009-03.htm",0,"30009-04.htm",],1,RECOMMENDATION_01],
30012:[0,["tutolutador-1.htm","30009-03.htm",0,"30009-04.htm",],1,RECOMMENDATION_01],
30056:[0,["tutolutador-1.htm","30009-03.htm",0,"30009-04.htm",],1,RECOMMENDATION_01],
30018:[0,["tutomage-1.htm",0,"tutomage-2.htm","tutomage-4.htm",],1,RECOMMENDATION_02],
30019:[0,["tutomage-1.htm",0,"tutomage-2.htm","30019-04.htm",],1,RECOMMENDATION_02],
30020:[0,["tutomage-1.htm",0,"tutomage-2.htm","tutomage-4.htm",],1,RECOMMENDATION_02],
30021:[0,["tutomage-1.htm",0,"tutomage-2.htm","tutomage-4.htm",],1,RECOMMENDATION_02],
#ELFOS
30370:[1,["30370-01.htm","30370-02.htm","30370-04.htm"],0,0],
30400:[1,["tutomage-1.htm","tutolutador-2.htm","tutomage-2.htm","30400-04.htm",],1,LEAF_OF_MOTHERTREE],
#DELFOS
30129:[2,["30129-01.htm","30129-02.htm","30129-04.htm"],0,0],
30131:[2,["tutomage-1.htm","tutolutador-2.htm","tutomage-2.htm","30131-04.htm",],1,BLOOD_OF_JUNDIN],
#KAMAEL
32133:[5,["32133-01.htm","32133-02.htm","32133-04.htm"],0,0],
32140:[5,["32134-01.htm","32134-03.htm",0,"32134-04.htm",],1,DIPLOMA]
}   
 
class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onAdvEvent(self,event,npc,player):
    st = player.getQuestState(qn)
    if not st: return
    htmltext = event
    qs = st.getPlayer().getQuestState(qnTutorial)
    if not qs: return
    player = st.getPlayer() 
    if qs != None :
       Ex = int(qs.get("Ex"))
       classId = int(st.getPlayer().getClassId().getId())
       
       if event == "TimerEx_NewbieHelper" :
          if Ex == 0 :
             if player.getClassId().isMage() :
                st.playTutorialVoice("tutorial_voice_009b")
             else :
                st.playTutorialVoice("tutorial_voice_009a")
             qs.set("Ex","1")
             
          elif Ex == 3 :
             st.playTutorialVoice("tutorial_voice_010a")
             qs.set("Ex","4")
          return
          
       elif event == "TimerEx_GrandMaster" :
          if Ex >= 4 :
             st.showQuestionMark(7)
             st.playSound("ItemSound.quest_tutorial")
             st.playTutorialVoice("tutorial_voice_025")
          return
         #KAMAEL TUTORIAL 
       elif event == "isle" :
          #st.addRadar(-124684,38775,1176)
          st.playTutorialVoice("tutorial_voice_030")
          htmltext = "<html><body>"+npc.getName()+":<br><br>Fale com :<br><center><br><img src=aic.npc width=64 height=64></center><br> Nome : <font color=\"00FF00\">Menu Principal</font> para Iniciar sua aventura.<br> Boa Sorte!</body></html>"
       else :
          htmlfile,radarX,radarY,radarZ,item,classId1,gift1,count1,classId2,gift2,count2 = EVENTS[event]
          if radarX != 0:
             st.addRadar(radarX,radarY,radarZ);
          htmltext=htmlfile
          if st.getQuestItemsCount(item) and st.getInt("onlyone") == 0:
             st.addExpAndSp(0,0)
             st.startQuestTimer("TimerEx_GrandMaster",60000)
             st.takeItems(item,1)
             if Ex <= 3 :
                qs.set("Ex","4")
             if st.getPlayer().getClassId().getId() == classId1 :
                st.giveItems(gift1,count1)
                if gift1 == SPIRITSHOT_NOVICE :
                   st.playTutorialVoice("tutorial_voice_027")
                else:
                   st.playTutorialVoice("tutorial_voice_026")
             elif st.getPlayer().getClassId().getId() == classId2 :
                if gift2:
                   st.giveItems(gift2,count2)
                   st.playTutorialVoice("tutorial_voice_026")
             st.unset("step")
             st.set("onlyone","1")
    return htmltext

 def onFirstTalk (self,npc,player):
   qs = player.getQuestState(qnTutorial)
   if not qs : 
      npc.showChatWindow(player)
      return None
   st = player.getQuestState(qn)
   if not st :
      st = self.newQuestState(player)
   htmltext = ""
   Ex = qs.getInt("Ex")
   npcId = npc.getNpcId()
   step=st.getInt("step")
   onlyone=st.getInt("onlyone")
   level=player.getLevel()
   isMage = player.getClassId().isMage()
   npcTyp=0
   
   if npcId in TALKS.keys():
      raceId,htmlfiles,npcTyp,item = TALKS[npcId]
   if (level >= 40 or onlyone) and npcTyp == 1:
       htmltext = "30575-05.htm"
   elif npcId in [30600, 30601, 30602, 30598, 30599, 32135 ]:
     reward=qs.getInt("reward")
     if reward == 0:
       if isMage :
         st.playTutorialVoice("tutorial_voice_027")
         st.giveItems(SPIRITSHOT_NOVICE,100)
       else:
         st.playTutorialVoice("tutorial_voice_026")
         st.giveItems(SOULSHOT_NOVICE,200)
       st.giveItems(TOKEN,10)
       st.giveItems(SCROLL,10)
       qs.set("reward","1")
       st.exitQuest(False)
     npc.showChatWindow(player)
     return None
   elif onlyone == 0 and level < 40 :
    if player.getRace().ordinal() == raceId :
      htmltext=htmlfiles[0]
      if npcTyp==1:
       if step==0 and Ex < 0:
        qs.set("Ex","0")
        st.startQuestTimer("TimerEx_NewbieHelper",50000)
        if isMage :
         st.set("step","1")
         st.setState(State.STARTED)
        else:
        #PARA QUEM NAO FOR MAGO
         htmltext="tutolutador-1.htm"
         st.set("step","1")
         st.setState(State.STARTED)
         
       elif step==1 and st.getQuestItemsCount(item)==0 and Ex in [0,1,2]:
         if st.getQuestItemsCount(BLUE_GEM) :
           st.takeItems(BLUE_GEM,st.getQuestItemsCount(BLUE_GEM))
           st.giveItems(item,1)
           st.set("step","2")
           qs.set("Ex","3")
           st.startQuestTimer("TimerEx_NewbieHelper",60000)
           qs.set("ucMemo","3")
           #SE FOR MAGO
           if isMage :
             st.playTutorialVoice("tutorial_voice_027")
             st.giveItems(SPIRITSHOT_NOVICE,200)
             htmltext = htmlfiles[2]
             if htmltext == 0 :
                 htmltext = "<html><body>Fale com Newbie Helper</body></html>"
           #SE NAO FOR MAGO
           else:
             st.playTutorialVoice("tutorial_voice_026")
             st.giveItems(SOULSHOT_NOVICE,200)
             htmltext = htmlfiles[1]
             if htmltext == 0 :
                 htmltext = "<html><body>Fale Com Newbie Helper.</body></html>"
         else:
           if isMage :
             htmltext = "tutomage-1.htm"
             if player.getRace().ordinal() == 3 :
              htmltext = "tutomage-1.htm"
           else:
             htmltext = "tutolutador-1.htm"
       elif step==2 :
        htmltext = htmlfiles[3]
      elif npcTyp == 0 :
        if step==1 :
          htmltext = htmlfiles[0]
        elif step==2 :
          htmltext = htmlfiles[1]
        elif step==3 :
          htmltext = htmlfiles[2]
   elif st.getState() == State.COMPLETED and npcTyp == 0:
     htmltext = str(npc.getNpcId())+"-04.htm"
   if htmltext == None or htmltext == "":
     npc.showChatWindow(player)
   return htmltext

 def onKill(self,npc,player,isPet):
   st = player.getQuestState(qn)
   if not st : return
   qs = st.getPlayer().getQuestState(qnTutorial)
   if not qs : return
   Ex = int(qs.get("Ex"))
   if qs != None :
      if Ex in [0,1] :
         st.playTutorialVoice("tutorial_voice_011")
         st.showQuestionMark(3)
         qs.set("Ex","2")
      if Ex in [0,1,2] and st.getQuestItemsCount(6353) < 1 :
         if st.getRandom(100) < 95 :
            st.dropItem(npc,player,6353,1)
            st.playSound("ItemSound.quest_tutorial")
   return

QUEST       = Quest(999,qn,"Dragon Tutorial")

for startNpc in [30008,30009,30017,30019,30129,30131,30573,30575,30370,30528,30530,30400,30401,30402,30403,30404,30600,30601,30598,30599,32133,32135,32140]:
  QUEST.addStartNpc(startNpc)
  QUEST.addFirstTalkId(startNpc)
  QUEST.addTalkId(startNpc)

QUEST.addKillId(18342)
QUEST.addKillId(20004)
QUEST.addKillId(20001)