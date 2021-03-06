/*
 * This program is free software: you can redistribute it and/or modify it under
 * the terms of the GNU General Public License as published by the Free Software
 * Foundation, either version 3 of the License, or (at your option) any later
 * version.
 * 
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
 * details.
 * 
 * You should have received a copy of the GNU General Public License along with
 * this program. If not, see <http://www.gnu.org/licenses/>.
 */
package net.sf.l2j.gameserver.handler.bypasshandlers;

import java.util.List;

import javolution.text.TextBuilder;
import javolution.util.FastList;
import net.sf.l2j.Config;
import net.sf.l2j.gameserver.cache.HtmCache;
import net.sf.l2j.gameserver.handler.IBypassHandler;
import net.sf.l2j.gameserver.instancemanager.QuestManager;
import net.sf.l2j.gameserver.model.actor.L2Character;
import net.sf.l2j.gameserver.model.actor.L2Npc;
import net.sf.l2j.gameserver.model.actor.instance.L2PcInstance;
import net.sf.l2j.gameserver.model.quest.Quest;
import net.sf.l2j.gameserver.model.quest.QuestState;
import net.sf.l2j.gameserver.model.quest.State;
import net.sf.l2j.gameserver.network.SystemMessageId;
import net.sf.l2j.gameserver.network.serverpackets.ActionFailed;
import net.sf.l2j.gameserver.network.serverpackets.SystemMessage;

public class QuestLink implements IBypassHandler
{
	private static final String[] COMMANDS =
	{
		"Quest"
	};

	public boolean useBypass(String command, L2PcInstance activeChar, L2Character target)
	{
		if (!(target instanceof L2Npc))
			return false;

		String quest = "";
		try
		{
			quest = command.substring(5).trim();
		}
		catch (IndexOutOfBoundsException ioobe)
		{
		}
		if (quest.length() == 0)
			showQuestWindow(activeChar, (L2Npc)target);
		else
			showQuestWindow(activeChar, (L2Npc)target, quest);

		return true;
	}

	/**
	 * Open a choose quest window on client with all quests available of the L2NpcInstance.<BR><BR>
	 * [TELA DE SELECAO DE QUESTS DO L2DRAGON, CREDITOS NA PAGINA]
	 * 
	 * <B><U> Actions</U> :</B><BR><BR>
	 * <li>Send a Server->Client NpcHtmlMessage containing the text of the L2NpcInstance to the L2PcInstance </li><BR><BR>
	 * 
	 * [OQUE FAZ?]
	 * [COLOCA OS OBJETOS (QUESTS) EM BOTOES]
	 * [DESCRICAO DOS ESTADOS DO OBJETOS (EM PROGRESSO, REALIZADO)
	 * [L2DRAGON PTBR]
	 * 
	 * @param player The L2PcInstance that talk with the L2NpcInstance
	 * @param quests The table containing quests of the L2NpcInstance
	 * 
	 */
	public static void showQuestChooseWindow(L2PcInstance player, L2Npc npc, Quest[] quests)
	{		
        TextBuilder sb = new TextBuilder();
        sb.append("<html><body><title>Sele????????o de Miss????o</title>");
        sb.append("<center>");
        sb.append("<font color=\"LEVEL\">Em Progresso</font> = Miss????o em andamento.<br1>");
        sb.append("<font color=\"00FF00\">Realizado</font> = Miss????o finalizada.<br>(ainda Pode haver intera????????o.)<br><br>");
        sb.append("<font color=\"C0C0CA\"> se vazio </font>= Pode ou N????o haver Miss????o.<br>");
        sb.append("Miss????o: <br>");
        for (Quest q : quests) 
        {
        	sb.append("<button value=\" ").append(q.getDescr()).append("\" action=\"bypass -h npc_").append(npc.getObjectId())
        	.append("_Quest ").append(q.getName()).append("\" width=188 height=38 back=\"L2UI_ct1.button_df\" fore=\"L2UI_ct1.button_df\">").append("Status => ");
       	
        	QuestState qs = player.getQuestState(q.getScriptName());
        	if (qs != null)
        	{        		
        		if (qs.getState() == State.STARTED && qs.getInt("cond") > 0)
        		{
        			sb.append("<font color=\"LEVEL\"> (Em Progresso) </font>");
        		}
        		else if (qs.getState() == State.COMPLETED )
       			{
        			sb.append("<font color=\"00FF00\"> (Realizado) </font>");
       			}
        	}
        	sb.append("<br>");
        	}
        
        	sb.append("<center>L2 Dragon</center><br>");
        sb.append("</body></html>");;

		// Send a Server->Client packet NpcHtmlMessage to the L2PcInstance in order to display the message of the L2NpcInstance
		npc.insertObjectIdAndShowChatWindow(player, sb.toString());
	}

	/**
	 * Open a quest window on client with the text of the L2NpcInstance.<BR><BR>
	 * 
	 * <B><U> Actions</U> :</B><BR><BR>
	 * <li>Get the text of the quest state in the folder data/scripts/quests/questId/stateId.htm </li>
	 * <li>Send a Server->Client NpcHtmlMessage containing the text of the L2NpcInstance to the L2PcInstance </li>
	 * <li>Send a Server->Client ActionFailed to the L2PcInstance in order to avoid that the client wait another packet </li><BR><BR>
	 * 
	 * @param player The L2PcInstance that talk with the L2NpcInstance
	 * @param questId The Identifier of the quest to display the message
	 * 
	 */
	public static void showQuestWindow(L2PcInstance player, L2Npc npc, String questId)
	{
		String content = null;

		Quest q = QuestManager.getInstance().getQuest(questId);

		// Get the state of the selected quest
		QuestState qs = player.getQuestState(questId);

		if (q == null)
		{
			// SEM QUESTS
			content = "<html><body>Sem os requisitos.</body></html>";
		}
		else
		{
			if ((q.getQuestIntId() >= 1 && q.getQuestIntId() < 20000) && (player.getWeightPenalty() >= 3 || player.getInventoryLimit() * 0.8 <= player.getInventory().getSize()))
			{
				player.sendPacket(new SystemMessage(SystemMessageId.INVENTORY_LESS_THAN_80_PERCENT));
				return;
			}

			if (qs == null)
			{
				if (q.getQuestIntId() >= 1 && q.getQuestIntId() < 20000)
				{
					Quest[] questList = player.getAllActiveQuests();
					if (questList.length >= 25) // if too many ongoing quests, don't show window and send message
					{
						player.sendPacket(new SystemMessage(SystemMessageId.TOO_MANY_QUESTS));
						return;
					}
				}
				// check for start point
				Quest[] qlst = npc.getTemplate().getEventQuests(Quest.QuestEventType.QUEST_START);

				if (qlst != null && qlst.length > 0)
				{
					for (Quest temp : qlst)
					{
						if (temp == q)
						{
							qs = q.newQuestState(player);
							break;
						}
					}
				}
			}
		}

		if (qs != null)
		{
			// If the quest is alreday started, no need to show a window
			if (!qs.getQuest().notifyTalk(npc, qs))
				return;

			questId = qs.getQuest().getName();
			String stateId = State.getStateName(qs.getState());
			String path = "data/scripts/quests/" + questId + "/" + stateId + ".htm";
			content = HtmCache.getInstance().getHtm(player.getHtmlPrefix(), path); //TODO path for quests html

			if (Config.DEBUG)
			{
				if (content != null)
				{
					_log.fine("Showing quest window for quest " + questId + " html path: " + path);
				}
				else
				{
					_log.fine("File not exists for quest " + questId + " html path: " + path);
				}
			}
		}

		// Send a Server->Client packet NpcHtmlMessage to the L2PcInstance in order to display the message of the L2NpcInstance
		if (content != null)
			npc.insertObjectIdAndShowChatWindow(player, content);

		// Send a Server->Client ActionFailed to the L2PcInstance in order to avoid that the client wait another packet
		player.sendPacket(ActionFailed.STATIC_PACKET);
	}

	/**
	 * Collect awaiting quests/start points and display a QuestChooseWindow (if several available) or QuestWindow.<BR><BR>
	 * 
	 * @param player The L2PcInstance that talk with the L2NpcInstance
	 * 
	 */
	public static void showQuestWindow(L2PcInstance player, L2Npc npc)
	{
		// collect awaiting quests and start points
		List<Quest> options = new FastList<Quest>();

		QuestState[] awaits = player.getQuestsForTalk(npc.getTemplate().npcId);
		Quest[] starts = npc.getTemplate().getEventQuests(Quest.QuestEventType.QUEST_START);

		// Quests are limited between 1 and 999 because those are the quests that are supported by the client.  
		// By limiting them there, we are allowed to create custom quests at higher IDs without interfering  
		if (awaits != null)
		{
			for (QuestState x : awaits)
			{
				if (!options.contains(x.getQuest()))
					if ((x.getQuest().getQuestIntId() > 0) && (x.getQuest().getQuestIntId() < 20000))
						options.add(x.getQuest());
			}
		}

		if (starts != null)
		{
			for (Quest x : starts)
			{
				if (!options.contains(x))
					if ((x.getQuestIntId() > 0) && (x.getQuestIntId() < 20000))
						options.add(x);
			}
		}

		// Display a QuestChooseWindow (if several quests are available) or QuestWindow
		if (options.size() > 1)
		{
			showQuestChooseWindow(player, npc, options.toArray(new Quest[options.size()]));
		}
		else if (options.size() == 1)
		{
			showQuestWindow(player, npc, options.get(0).getName());
		}
		else
		{
			showQuestWindow(player, npc, "");
		}
	}

	public String[] getBypassList()
	{
		return COMMANDS;
	}
}