package com.perso.constant;

import java.util.Arrays;

public enum VegetableSize {
    GRAND("grand"),
    MOYEN("moyen"),
    BAS("bas"),
    UNKNOWN("taille-inconnu");

    private String name;

    /**
     * Constructor.
     *
     * @param name of the vegetable size.
     */
    VegetableSize(String name) {
        this.name = name;
    }

    public static VegetableSize getVegetableSize(String size) {
        for(VegetableSize vegetableSize : Arrays.asList(VegetableSize.values())) {
            if(vegetableSize.name.equalsIgnoreCase(size)) {
                return vegetableSize;
            }
        }
        return UNKNOWN;
    }

    /**
     * retrieve vegetable size name.
     *
     * @return the name of the vegetable size.
     */
    public String getName() {
        return name;
    }

}
