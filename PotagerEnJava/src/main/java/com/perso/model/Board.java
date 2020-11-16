package com.perso.model;

import lombok.Data;

@Data
public class Board {

    private String midSquare;
    private String eastSquare;
    private String westSquare;
    private String northSquare;
    private String southSquare;
    private String northWestSquare;
    private String northEastSquare;
    private String southEastSquare;
    private String southWestSquare;

}
