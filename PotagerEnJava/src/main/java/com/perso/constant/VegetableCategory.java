package com.perso.constant;

import java.util.Arrays;

public enum VegetableCategory {
    GRAINE("legume-graine"),
    RACINE("legume-racine"),
    FEUILLE("legume-feuille"),
    FRUIT("legume-fruit"),
    UNKNOWN("categorie-inconnu");

    private String name;

    /**
     * Constructor.
     *
     * @param name of the vegetable category.
     */
    VegetableCategory(String name) {
        this.name = name;
    }

    public static VegetableCategory getVegetableCategory(String category) {
        for(VegetableCategory vegetableCategory : Arrays.asList(VegetableCategory.values())) {
            if(vegetableCategory.name.equalsIgnoreCase(category)) {
                return vegetableCategory;
            }
        }
        return UNKNOWN;
    }

    /**
     * retrieve vegetable category name.
     *
     * @return the name of the vegetable category.
     */
    public String getName() {
        return name;
    }

}
