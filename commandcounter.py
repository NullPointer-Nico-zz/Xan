import os

Admin_Commands = set([])
Allegemeine_commands = set([])
mod_commands = set([])
owner_commands = set([])
alle_commands = set([])
fun_commands = set([])

for admin in os.listdir('./Admin_Commands'):
    if admin.endswith('.py'):
        Admin_Commands.add(admin)

for alle in os.listdir('./Allgemeine_commands'):
    if alle.endswith('.py'):
        Allegemeine_commands.add(alle)

for mod in os.listdir('./Mod_Commands'):
    if mod.endswith('.py'):
        mod_commands.add(mod)

for owner in os.listdir('./Owner_Commands'):
    if owner.endswith('.py'):
        owner_commands.add(owner)

for a in os.listdir('./Allgemeine_commands'):
    if a.endswith('.py'):
        alle_commands.add(a)

for aa in os.listdir('./Admin_Commands'):
    if aa.endswith('.py'):
        alle_commands.add(aa)

for m in os.listdir('./Mod_Commands'):
    if m.endswith('.py'):
        alle_commands.add(m)

for o in os.listdir('./Owner_Commands'):
    if o.endswith('.py'):
        alle_commands.add(o)

for f in os.listdir('./fun'):
    if f.endswith('.py'):
        alle_commands.add(f)

for fun in os.listdir('./fun'):
    if fun.endswith('.py'):
        fun_commands.add(fun)
