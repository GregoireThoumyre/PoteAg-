package com.perso.model;

import lombok.Data;

@Data
public class BoardOverTime {

    private Board currentBoard;
    private Board lastYearBoard;
    private Board twoYearsAgoBoard;
    private Board threeYearsAgoBoard;

}
