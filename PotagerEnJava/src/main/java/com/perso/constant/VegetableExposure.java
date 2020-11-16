package com.perso.constant;

import java.util.Arrays;

public enum VegetableExposure {
    NORD("nord"),
    EsT("est"),
    OUEST("ouest"),
    SUD("sud"),
    WHATEVER("peu importe");

    private String name;

    /**
     * Constructor.
     *
     * @param name of the vegetable exposure.
     */
    VegetableExposure(String name) {
        this.name = name;
    }

    public static VegetableExposure getVegetableExposure(String exposure) {
        for(VegetableExposure vegetableExposure : Arrays.asList(VegetableExposure.values())) {
            if(vegetableExposure.name.equalsIgnoreCase(exposure)) {
                return vegetableExposure;
            }
        }
        return WHATEVER;
    }

    /**
     * retrieve vegetable size name.
     *
     * @return the name of the vegetable exposure.
     */
    public String getName() {
        return name;
    }

}
