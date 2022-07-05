//QUEST GLUDIO DION DEPOIS DO LEVEL 37 
package quests.Q00161_FruitsOfMotherTree;

import net.sf.l2j.gameserver.model.actor.L2Npc;
import net.sf.l2j.gameserver.model.actor.instance.L2PcInstance;
import net.sf.l2j.gameserver.model.base.Race;
import net.sf.l2j.gameserver.model.quest.Quest;
import net.sf.l2j.gameserver.model.quest.QuestState;
import net.sf.l2j.gameserver.model.quest.State;

/**
 * Fruits Of MotherTree (161)
 * @author Tryskell
 */
public class Q00161_FruitsOfMotherTree extends Quest
{
	// Items
    private static final int MOTHERTREE_FRUIT = 1036;
    private static final int ANDELLRIAS_LETTER = 1037;
	
    //NPCs
    private static final int BELKIS = 32143;
    private static final int BASILLA = 30638;
    private static final int SWAN = 30957;	
    
	public Q00161_FruitsOfMotherTree()
	{
		super(161, Q00161_FruitsOfMotherTree.class.getSimpleName(), "Caminhos do Destino");
		registerQuestItems(MOTHERTREE_FRUIT,ANDELLRIAS_LETTER);
		addStartNpc(BELKIS);
		addTalkId(BELKIS, BASILLA, SWAN);
	}
	
	@Override
	public String onAdvEvent(String event, L2Npc npc, L2PcInstance player)
	{
		QuestState st = player.getQuestState(getName());
		if (st == null)
		{
			return getNoQuestMsg();
		}
		String htmltext = event;
		
		switch (event)
		{
			case "30362-04.htm":
				st.startQuest();
				st.giveItems(ANDELLRIAS_LETTER, 1);
				break;
		}
	    return htmltext;
	}
	
	@Override
	public String onTalk(L2Npc npc, L2PcInstance player)
	{
		final QuestState st = player.getQuestState(getName());
		String htmltext = getNoQuestMsg();
		if (st == null)
		{
			return htmltext;
		}
		switch (st.getState())
		{
			case State.CREATED:
			{
				if (st.getQuestItemsCount(163) == 1)
					htmltext = "30362-00.htm";
				else if (player.getLevel() < 37)
					htmltext = "30362-02.htm";
				else
					htmltext = "30362-03.htm";
				break;
			}
			case State.COMPLETED:
				htmltext = "finish.htm";
				
			case State.STARTED:
				int cond = st.getInt("cond");
				switch (npc.getNpcId())
				{
					case BELKIS:
						if (cond == 1)
							htmltext = "30362-05.htm";
						break;
						
					case BASILLA:
						if (cond == 1)
						{
							htmltext = "30371-01.htm";
							st.set("cond", "2");							st.playSound(QuestSound.ITEMSOUND_QUEST_MIDDLE);
							st.takeItems(ANDELLRIAS_LETTER, 1);
							st.giveItems(MOTHERTREE_FRUIT, 1);  
						}
						else if (cond == 2)
							htmltext = "30371-02.htm";
						break;
						// CUSTOM 
					case SWAN:
						if (cond == 2)
						{
							htmltext = "30362-06.htm";
							st.takeItems(MOTHERTREE_FRUIT, 1);
							st.rewardItems(57, 3000000);
							st.rewardItems(2131, 50);
							st.addExpAndSp(50000, 0);
							st.playSound(QuestSound.ITEMSOUND_QUEST_FINISH);
							st.exitQuest(false);
						}
						break;						
				}
				break;
		}
		return htmltext;
	}
	
	public static void main(String[] args)
	{
		new Q00161_FruitsOfMotherTree();
	}
}
