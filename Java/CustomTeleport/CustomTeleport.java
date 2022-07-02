package teleports.CustomTeleport;

import net.sf.l2j.gameserver.datatables.DoorTable;
import net.sf.l2j.gameserver.model.actor.L2Npc;
import net.sf.l2j.gameserver.model.actor.instance.L2PcInstance;
import net.sf.l2j.gameserver.model.quest.Quest;
//import net.sf.l2j.gameserver.model.quest.QuestState;

public class CustomTeleport extends Quest
{	
	public CustomTeleport(int questId, String name, String descr)
	{
		super(questId, name, descr);// extends Quest (Classe Pai)
		//addFirstTalkId(32039,32040);//Primeiro contato como NPC
		addFirstTalkId(70000,70001);
		addStartNpc(70000,70001);
		addTalkId(70000,70001);
	}
	//Eventos
	
	
	@Override
	public String onAdvEvent(String event, L2Npc npc, L2PcInstance player)
	{	
	    if (event.equalsIgnoreCase("Close_Door1"))
	        DoorTable.getInstance().getDoor(19160001).closeMe();
	    else if (event.equalsIgnoreCase("Close_Door2"))
	        DoorTable.getInstance().getDoor(19160010).closeMe();
	        DoorTable.getInstance().getDoor(19160011).closeMe();
	     return null;
	}
	
	//PRIMEIRO CONTATO
	@Override
	public String onFirstTalk (L2Npc npc,L2PcInstance player)
	{
	    int npcId = npc.getNpcId();
	    
	    if (npcId == 70000)
	    	player.teleToLocation(45691,46007,-2998);
	    else if (npcId == 70001)
	    	player.teleToLocation(36640,-51218,718);
	    return "";
	}
	// @Override
	// public String onTalk(L2Npc npc, L2PcInstance player)
	// {
	   // QuestState st = player.getQuestState(getName());
	   // int npcId = npc.getNpcId();
	   // String htmltext = null;
	   
	    // if (npcId == 32034)
	    // {
	        // if (st.getQuestItemsCount(8064) == 0 && st.getQuestItemsCount(8065) == 0 && st.getQuestItemsCount(8067) == 0)
	            // return "<html><body>The Temple Gatekeeper:<br>You have nothing that would cover the holes.<br>(You must have a Visitor's Mark, a Faded Visitor's Mark, or a Pagan's Mark in order to open this door.)</body></html>";
	        
	        // htmltext = "FadedMark.htm";
	        // DoorTable.getInstance().getDoor(19160001).openMe();
	        // startQuestTimer("Close_Door1",10000,null,null);
	    // }
	        
	    // else if (npcId == 32035)
	    // {
	    	// DoorTable.getInstance().getDoor(19160001).openMe();
	    	// startQuestTimer("Close_Door1",10000,null,null);
	    	// htmltext = "FadedMark.htm";
	    // }
	    // else if (npcId == 32036)
	    // {
	        // if (!st.hasQuestItems(8067))
	        // {
	          // htmltext = "<html><body>The Temple Gatekeeper:<br>Show your Mark or be gone from my sight!<br>Only those who possess the Pagan's Mark may pass through this gate!</body></html>";
	        // }
	        // else
	        // {
	          // htmltext = "<html><body>The Temple Gatekeeper:<br>On seeing the Pagan's Mark, the statue's probing eyes go blank.<br>With the quiet whir of an engine, the gate swings open...</body></html>";
	          // startQuestTimer("Close_Door2",10000,null,null);
	          // DoorTable.getInstance().getDoor(19160010).openMe();
	          // DoorTable.getInstance().getDoor(19160011).openMe();
	        // }
	    // }
	    // else if (npcId == 32037)
	    // {
	        // DoorTable.getInstance().getDoor(19160010).openMe();
	        // DoorTable.getInstance().getDoor(19160011).openMe();
	        // startQuestTimer("Close_Door2",10000,null,null);
	        // htmltext = "FadedMark.htm";
	    // }

	    // else if (npcId == 32039)
	    // {
	    	// player.teleToLocation(-12766, -35840, -10856);
	    // }

	    // else if (npcId == 32040)
	    // {
	    	// player.teleToLocation(34962, -49758, -763);
	    // }
	    // st.exitQuest(true);
	    // return htmltext;
	// }

	public static void main(String[] args)
	{
		new CustomTeleport(-1, "CustomTeleport", "custom");
	}
}