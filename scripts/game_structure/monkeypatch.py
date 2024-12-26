import i18n

from scripts.cat.cats import Cat
from scripts.game_structure.game_essentials import game
from scripts.utility import event_text_adjust

# please for the love of GOD don't do this. ever.

groups = ["m_c", "r_c", "p_l", "s_c", "mur_c"]
other = [
    "dep_name",
    "lead_name",
    "med_name",
    "patrol_cats",
    "patrol_apprentices",
    "new_cats",
    "multi_cats",
    "clan",
    "other_clan",
    "chosen_herb",
]


def translate(text: str, **kwargs):
    if text == "":
        return ""
    if text == "screens.core.cat_list":
        print("cat_list loading")
        print("kwargs:", [kwarg for kwarg in kwargs])
    output = i18n.t(text, **kwargs)
    if output == "screens.core.cat_list":
        print("cat_list name unchanged")
    elif output == "Cat List":
        print("cat_list successfully pulled from i18n")
    dict = {}
    for cat in groups:
        if cat in kwargs and cat in output:
            if text == "screens.core.cat_list":
                print("cat found? ", str(cat))
            dict[cat] = kwargs[cat]
    for role in other:
        if role in kwargs:
            dict[role] = kwargs[role]
    if dict is not None:
        return event_text_adjust(
            Cat,
            output,
            patrol_leader=dict.get("p_l"),
            main_cat=dict.get("m_c"),
            random_cat=dict.get("r_c"),
            stat_cat=dict.get("s_c"),
            victim_cat=dict.get("mur_c"),
            patrol_cats=dict.get("patrol_cats"),
            patrol_apprentices=dict.get("patrol_apprentices"),
            new_cats=dict.get("new_cats"),
            multi_cats=dict.get("multi_cats"),
            clan=dict.get("clan", game.clan),
            other_clan=dict.get("other_clan"),
            chosen_herb=dict.get("chosen_herb"),
        )
    return output
