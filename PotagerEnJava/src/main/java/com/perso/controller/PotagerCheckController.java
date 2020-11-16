package com.perso.controller;

import com.perso.service.VegetableLoader;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/check")
public class PotagerCheckController {

    private VegetableLoader vegetableLoader;

    protected PotagerCheckController(VegetableLoader vegetableLoader) {
        this.vegetableLoader = vegetableLoader;
    }

    @GetMapping(value = "/checkDictionary", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<List<String>> checkDictionary () {
        return new ResponseEntity<>(vegetableLoader.checkDataFromDictionary(), HttpStatus.OK);
    }

}
