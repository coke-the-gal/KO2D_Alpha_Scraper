import praw
import re
import os
import numpy

regray = ['🎲 \+(.+?) Base Roll', '[⚔✨🏹] [\+-]\d+ (.+?) XP', '📚 (.+?) ', '[⚔✨🏹] [+-]\d (.+?)\n[⚔✨🏹]', '[⚔️✨🏹] \+(\d) \w.+\n[⚔️✨🏹]', '[⚔⏬] (.+?) Item Type', '[⏬🌟] (.)\d', '[⏬🌟] [+-](.+?) Element', '🎯 (.+?)x', '💥 -(.+?) HP', '\*\*\(🛡️ (Block)\)\*\*', ' \+(.+?) New Player', '\*\*(.+?)\*\* Total Damage', '(\d+) Gold', '[⚔️✨🏹] \+(.+?) \w+ XP', '💖 \+(\d+) Constitution', '🏅  \+(.\d+) RP']
#order is dmg_base_reg, type_reg, dmg_type_reg, item_reg, dmg_item_reg, m_type_reg, m_element_reg, dmg_element_reg, crit_reg, sub_HP_reg, block_reg, new_p_reg, t_dmg_reg, gold_reg, exp_type_reg, exp_con_reg, rp_reg

reddit = praw.Reddit(
    client_id="NAREl1tpNRYSbGBGrfZJ_w",
    client_secret="PdneWwNGiGwdPXG4plrKiwVSBIii_A",
    user_agent="KOTD Scrapper",
    username="coke_the_gal",
)

subreddit = reddit.subreddit('kickopenthedoor')
new_pyth = subreddit.new(limit=125)
for submission in new_pyth:
    if not submission.stickied:
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            if not comment.stickied and submission.author == comment.author and 'Damage Breakdown' in comment.body:
                with open(r'C:\Users\cokeb\Desktop\PROJECT SISTER\Little Sister\Data Set Beta\data.txt', 'a', encoding='utf8') as file:
                    comment = str(comment.body)
                    comment = comment.replace('|','|\n')
                    comment = comment.replace('|','')
                    comment = comment.replace(':-','')
                    comment = comment.replace('Damage Breakdown','')
                    comment = comment.replace('Player Breakdown','')
                    comment = comment.replace('Come join our discord at https://discord.gg/kotd!','')
                    test = []
                    i = 0
                    while i < 17:
                        test.append(re.search(regray[i], comment).group(1) if re.search(regray[i], comment) is not None else '')
                        i += 1
                    test.append(re.search('\[Health:(\d+)\]', submission.title).group(1))
                    i = 0
                    file.write(str(test)+"\n")
                    file.close()

print(regray)

