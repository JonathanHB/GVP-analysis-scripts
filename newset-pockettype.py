#make figures showing different types of pocket using the new set proteins

#mode key:
    #0: loop motion
    #1: secondary structure element separation
    #2: secondary structure change
    #3: interdomain motion
mode = 2

inputdict = [
    ["2w9tA", "2w9sC",
      "0.438027114,   -0.447464436,    0.779674649,\
       0.568756044,    0.809594870,    0.145111203,\
      -0.696155727,    0.379892021,    0.609122396,\
       0.000094447,    0.000033122,  -90.008842468,\
      25.788772583,   16.619495392,   10.260643959,\
      67.439460754,  112.538200378,  -20.000000000"], #loop motion
    ["3rwvA", "3s0kA",
     "-0.614209414,    0.291887611,   -0.733151913,\
       0.205862507,   -0.837621152,   -0.505952477,\
      -0.761798322,   -0.461694509,    0.454386890,\
       0.001110850,    0.001121301, -108.766372681,\
       7.980000496,   19.918218613,   51.464557648,\
      84.955223083,  132.526641846,  -20.000000000"], #secondary structure motion
    ["1y1aA","1y1aB",
     "-0.915403366,   -0.379530638,   -0.134002820,\
      -0.387331247,    0.740113497,    0.549717665,\
      -0.109465688,    0.555123150,   -0.824514270,\
      -0.000102934,   -0.003038038, -129.492019653,\
      10.123163223,   60.902191162,  143.110015869,\
      96.192573547,  163.445648193,  -20.000000000"], #secondary structure change
    ["4p0iB","5otaA",
     "-0.601927102,    0.746061087,    0.284674466,\
      -0.182281733,    0.218713894,   -0.958599865,\
      -0.777451634,   -0.628902256,    0.004341412,\
       0.000108700,    0.002309909, -121.331329346,\
     -47.176174164,  -17.714878082,   37.064323425,\
      87.706649780,  154.959793091,  -20.000000000"]  #interdomain motion (reverse)
    ]

    #proteins of interest
apo = inputdict[mode][0] #"3rwvA"
holo = inputdict[mode][1] #"3s0kA"
view = inputdict[mode][2]

    #clear previous structures
cmd.delete("all")

    #load and align structures
cmd.fetch(apo)
cmd.fetch(holo)

cmd.align(holo, apo)

    #graphics settings

#define secondary structure consistently
cmd.dss()

#cartoon rendering
cmd.set("cartoon_fancy_helices", "on")

#lighting
cmd.set("spec_reflect", "off")

#colors
cmd.bg_color("white")

cmd.color("grey", apo)
cmd.color("marine", holo)

util.cbam("not polymer.protein") #color ligand

#showing and hiding things
cmd.hide("spheres")
cmd.hide("nonbonded")
cmd.hide("everything", "element H")

cmd.hide("everything", "resn GOL+EDO")

    #view
cmd.set_view(view)

    #save figure
cmd.png(f"figures/{apo}_opening")
