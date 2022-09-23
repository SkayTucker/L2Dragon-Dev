	public static void showQuestWindowChoose(Player player, Npc npc, List<Quest> quests)
	{
		final StringBuilder sb = new StringBuilder("<html><body><title>Selecionar Quests</title>");
		sb.append("<br>");
		StringUtil.append(sb, "<center><font color=\"LEVEL\">Em Progresso</font> = Quest em andamento.<br1>");
		StringUtil.append(sb, "<center><font color=\"00FF00\">Realizado</font> = Quest finalizada.<br>");
		StringUtil.append(sb, "<center><font color=\"C0C0CA\">( vazio ) </font>= Disponivel<br>");
		sb.append("<img src=\"L2UI.SquareGray\" width=300 height=5>");
		StringUtil.append(sb, "<center> Quest disponives:<br>");
      
		for (Quest q : quests)
		{
			StringUtil.append(sb, "<center><button value=\"",q.getDescr(),"\" action=\"bypass -h npc_%objectId%_Quest ", q.getName(), "\" width=170 height=30 back=\"botoes.buffer_big_btn_over\" fore=\"botoes.buffer_big_btn\"> Status => ");
			
			final QuestState qs = player.getQuestState(q.getName());
			if (qs != null && qs.isStarted())
				
				sb.append("<center><font color=\"LEVEL\"> (Em Progresso) </font>");
			
			else if (qs != null && qs.isCompleted())
				sb.append("<center><font color=\"00FF00\"> (Realizado) </font>");
			else
				sb.append("<br>");
		}
		sb.append("<center><font color=\"FFFF00\">L2 Dragon</font> - <font color=\"B0E0E6\">Interlude</font></center><br>");
		sb.append("</body></html>");
		
		final NpcHtmlMessage html = new NpcHtmlMessage(npc.getObjectId());
		html.setHtml(sb.toString());
		html.replace("%objectId%", npc.getObjectId());
		player.sendPacket(html);
		
		player.sendPacket(ActionFailed.STATIC_PACKET);
	}
