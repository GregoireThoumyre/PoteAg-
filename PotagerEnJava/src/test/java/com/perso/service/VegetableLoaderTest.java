package com.perso.service;

import com.perso.config.CsvHeaderProperties;
import com.perso.model.Vegetable;
import junit.framework.Assert;
import org.junit.jupiter.api.Test;

import java.net.URL;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class VegetableLoaderTest {
    private CsvHeaderProperties csvHeaderProperties;

    public void init() {
        CsvHeaderProperties csvHeaderProperties = new CsvHeaderProperties();
        csvHeaderProperties.setHeader(true);
        URL dictionaryUrl = getClass().getClassLoader().getResource("dictionary");
        if (dictionaryUrl != null) {
            csvHeaderProperties.setLocation(dictionaryUrl.getPath());
        }
        csvHeaderProperties.setSeparator(";");
        this.csvHeaderProperties = csvHeaderProperties;
    }

    @Test
    public void should_read_the_dictionary_files_and_map_them() {
        // GIVEN
        init();
        Map<String, Vegetable> expectedVegetableMap = new HashMap<>();
        expectedVegetableMap.put("AUBERGINE",
                Vegetable.builder()
                        .name("AUBERGINE")
                        .category("FRUIT")
                        .icon("AUBERGINE.PNG")
                        .location("MILIEU")
                        .size("UNKNOWN")
                        .sunshine("")
                        .description("")
                        .exposure("WHATEVER")
                        .farFrom(Collections.emptyList())
                        .closeFrom(Collections.emptyList())
                        .plantAfter(Collections.emptyList()).build());
        expectedVegetableMap.put("BASILIC",
                Vegetable.builder()
                        .name("BASILIC")
                        .category("FEUILLE")
                        .icon("BASILIC.PNG")
                        .exposure("SUD")
                        .location("WHATEVER")
                        .size("UNKNOWN")
                        .sunshine("PLEIN SOLEIL")
                        .description("")
                        .farFrom(Collections.emptyList())
                        .closeFrom(Collections.emptyList())
                        .plantAfter(Collections.emptyList()).build());
        expectedVegetableMap.put("COURGETTE",
                Vegetable.builder()
                        .name("COURGETTE")
                        .category("FRUIT")
                        .icon("COURGETTE.PNG")
                        .location("BORD")
                        .exposure("NORD")
                        .size("UNKNOWN")
                        .sunshine("")
                        .description("PALISSE")
                        .farFrom(Collections.emptyList())
                        .closeFrom(Collections.emptyList())
                        .plantAfter(Collections.emptyList()).build());
        VegetableLoader vegetableLoader = new VegetableLoader(csvHeaderProperties);

        // WHEN
        Map<String, Vegetable> actualVegetablesSet = vegetableLoader.loadDataFromCsvDirectory();

        // THEN
        actualVegetablesSet.forEach((name, actualVegetable) -> {
            if (expectedVegetableMap.get(name) == null) {
                Assert.fail();
            } else {
                assertVegetableAreEquals(expectedVegetableMap.get(name), actualVegetable);
            }
        });
        expectedVegetableMap.forEach((name, expectedVegetable) -> {
            if (actualVegetablesSet.get(name) == null) {
                Assert.fail();
            } else {
                assertVegetableAreEquals(expectedVegetable, actualVegetablesSet.get(name));
            }
        });

    }

    private void assertVegetableAreEquals(Vegetable expectedVegetable, Vegetable actualVegetable) {
        Assert.assertEquals(expectedVegetable.getName(), actualVegetable.getName());
        Assert.assertEquals(expectedVegetable.getCategory(), actualVegetable.getCategory());
        Assert.assertEquals(expectedVegetable.getCloseFrom(), actualVegetable.getCloseFrom());
        Assert.assertEquals(expectedVegetable.getDescription(), actualVegetable.getDescription());
        Assert.assertEquals(expectedVegetable.getExposure(), actualVegetable.getExposure());
        Assert.assertEquals(expectedVegetable.getFarFrom(), actualVegetable.getFarFrom());
        Assert.assertEquals(expectedVegetable.getLocation(), actualVegetable.getLocation());
        Assert.assertEquals(expectedVegetable.getPlantAfter(), actualVegetable.getPlantAfter());
        Assert.assertEquals(expectedVegetable.getSize(), actualVegetable.getSize());
        Assert.assertEquals(expectedVegetable.getSunshine(), actualVegetable.getSunshine());
    }

}
