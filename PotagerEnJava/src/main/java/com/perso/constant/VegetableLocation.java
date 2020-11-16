package com.perso.constant;

import java.util.Arrays;

public enum VegetableLocation {
    MILIEU("milieu"),
    PAS_AU_MILIEU("pas au milieu"),
    BORD("bord"),
    DEVANT_OU_BORD("devant ou bord"),
    ARRIERE("arriere"),
    WHATEVER("peu importe"),
    PARTOUT("partout"),
    BORD_PALISSE("bord palisse"),
    SPECIFIC_RULE("regles specifiques");

    private String name;

    /**
     * Constructor.
     *
     * @param name of the vegetable location.
     */
    VegetableLocation(String name) {
        this.name = name;
    }

    public static VegetableLocation getVegetableLocation(String location) {
        for(VegetableLocation vegetableLocation : Arrays.asList(VegetableLocation.values())) {
            if(vegetableLocation.name.equalsIgnoreCase(location)) {
                return vegetableLocation;
            }
        }
        return WHATEVER;
    }

    /**
     * retrieve vegetable category name.
     *
     * @return the name of the vegetable location.
     */
    public String getName() {
        return name;
    }

}
