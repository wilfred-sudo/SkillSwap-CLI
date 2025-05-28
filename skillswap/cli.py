import click

@click.command()
@click.argument('skill_name')
def show_offering(skill_name):
    session = Session()
    results = session.query(User).join(UserSkill).join(Skill).filter(
        Skill.name == skill_name,
        UserSkill.is_offering == True
    ).all()

    for user in results:
        print(f"{user.name} offers {skill_name}")
