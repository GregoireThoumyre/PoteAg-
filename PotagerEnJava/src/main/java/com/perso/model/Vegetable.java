package com.perso.model;

import com.perso.constant.*;
import lombok.*;
import org.codehaus.plexus.util.StringUtils;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class Vegetable {
    private String name;
    private String description;
    private String category;
    private String size;
    private String location;
    private String exposure;
    private String sunshine;
    private String icon;
    private List<String> farFrom;
    private List<String> closeFrom;
    private List<String> plantAfter;

    public Vegetable(String[] vegetableAsArray) {
        this.name = VegetableName.getVegetableName(vegetableAsArray[0]).name();
        this.category = VegetableCategory.getVegetableCategory(vegetableAsArray[1]).name();
        this.size = VegetableSize.getVegetableSize(vegetableAsArray[2]).name();
        this.icon = vegetableAsArray[3];
        this.location = VegetableLocation.getVegetableLocation(vegetableAsArray[4]).name();
        this.exposure = VegetableExposure.getVegetableExposure(vegetableAsArray[5]).name();
        this.sunshine = vegetableAsArray[6];
        this.description = vegetableAsArray[7];
        this.farFrom = getVegetableNamesAsList(vegetableAsArray[8]);
        this.closeFrom = getVegetableNamesAsList(vegetableAsArray[9]);
        this.plantAfter = getVegetableNamesAsList(vegetableAsArray[10]);
    }

    private List<String> getVegetableNamesAsList(String vegetableListAsString) {
        if (StringUtils.isEmpty(vegetableListAsString)) {
            return Collections.emptyList();
        }
        List<String> vegetableNamesList = new ArrayList<>();
        for (String vegetable : vegetableListAsString.split(",")) {
            if (!StringUtils.isEmpty(vegetable)) {
                vegetableNamesList.add(VegetableName.getVegetableName(vegetable.trim()).name());
            }
        }
        return vegetableNamesList;
    }
}
