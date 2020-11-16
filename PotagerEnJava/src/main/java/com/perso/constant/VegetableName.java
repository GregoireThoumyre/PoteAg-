package com.perso.constant;

import java.util.Arrays;

public enum VegetableName {
    AUBERGINE("AUBERGINE"),
    BASILIC("BASILIC"),
    BETTERAVE("BETTERAVE"),
    BROCOLI("BROCOLI"),
    CAROTTE("CAROTTE"),
    CELERI("CELERI"),
    CHICOREE("CHICOREE"),
    CHOU("CHOU"),
    CHOU_DE_CHINE("CHOU DE CHINE"),
    CONCOMBRE("CONCOMBRE"),
    CORNICHON("CORNICHON"),
    COURGETTE("COURGETTE"),
    EPINARD("EPINARD"),
    HARICOTS_GRIMPANTS("HARICOTS GRIMPANTS"),
    HARICOTS_NAINS("HARICOTS NAINS"),
    LAITUE("LAITUE"),
    MACHE("MACHE"),
    MESCLUN("MESCLUN"),
    NAVET("NAVET"),
    OIGNON_BLANC("OIGNON BLANC"),
    PERSIL("PERSIL"),
    POIREAU("POIREAU"),
    POIREE("POIREE"),
    POIS("POIS"),
    POIVRON("POIVRON"),
    RADIS("RADIS"),
    SALADE("SALADE"),
    TOMATE("TOMATE"),
    UNKNOWN("LEGUME-INCONNU");

    private String name;

    /**
     * Constructor.
     *
     * @param name of the vegetable name.
     */
    VegetableName(String name) {
        this.name = name;
    }

    public static VegetableName getVegetableName(String name) {
        for(VegetableName vegetableName : Arrays.asList(VegetableName.values())) {
            if(vegetableName.name.equalsIgnoreCase(name)) {
                return vegetableName;
            }
        }
        return UNKNOWN;
    }

    /**
     * retrieve vegetable category name.
     *
     * @return the name of the vegetable.
     */
    public String getName() {
        return name;
    }

}
