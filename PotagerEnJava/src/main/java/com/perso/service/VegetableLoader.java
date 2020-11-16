package com.perso.service;

import com.perso.PotagerEnJava;
import com.perso.config.CsvHeaderProperties;
import com.perso.constant.VegetableCategory;
import com.perso.constant.VegetableName;
import com.perso.constant.VegetableSize;
import com.perso.model.Vegetable;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class VegetableLoader {

    private final Logger LOGGER = LoggerFactory.getLogger(PotagerEnJava.class);

    private final CsvHeaderProperties csvHeaderProperties;

    /**
     * Constructor.
     */
    protected VegetableLoader(CsvHeaderProperties csvHeaderProperties) {
        this.csvHeaderProperties = csvHeaderProperties;
    }

    public Map<String, Vegetable> loadDataFromCsvDirectory() {
        Map<String, Vegetable> vegetableMap = new HashMap<>();

        for (String filepath : getFilePathToRead()) {
            vegetableMap.putAll(loadDataFromCsv(filepath));
        }

        return vegetableMap;
    }

    private List<String> getFilePathToRead() {
        List<String> filePathList = new ArrayList<>();

        File directoryLocation = new File(csvHeaderProperties.getLocation());
        if (directoryLocation.exists()) {
            if (directoryLocation.isDirectory()) {
                String[] fileList = directoryLocation.list();
                if (fileList != null && fileList.length != 0) {
                    for (String filePath : fileList) {
                        File file = new File(directoryLocation.getAbsolutePath() + "/" + filePath);
                        if (!file.isDirectory()) {
                            filePathList.add(file.getAbsolutePath());
                        }
                    }
                } else {
                    LOGGER.error("Directory location for csv data is empty");
                }
            } else {
                filePathList.add(directoryLocation.getAbsolutePath());
            }
        } else {
            LOGGER.error("Directory location for csv data doesn't exist : {}", csvHeaderProperties.getLocation());
        }
        return filePathList;
    }

    private Map<String, Vegetable> loadDataFromCsv(String csvFile) {
        Map<String, Vegetable> vegetableMap = new HashMap<>();
        String line;

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {

            if (csvHeaderProperties.getHeader()) {
                String header = br.readLine();
            }

            while ((line = br.readLine()) != null) {
                if (!csvHeaderProperties.getSeparator().equalsIgnoreCase(line.substring(line.length() - 1))) {
                    line += csvHeaderProperties.getSeparator();
                }
                String[] splittedLine = line.toUpperCase().split(csvHeaderProperties.getSeparator(), -1);
                Vegetable vegetable = new Vegetable(splittedLine);
                vegetableMap.put(vegetable.getName(), vegetable);
            }
        } catch (IOException e) {
            LOGGER.error("Error while reading csv file : {}, error : ", csvFile, e);
        }
        return vegetableMap;
    }

    public List<String> checkDataFromDictionary() {
        List<String> errorList = new ArrayList<>();
        for (String fileToCheck : getFilePathToRead()) {
            Map<String, Vegetable> vegetableMap = loadDataFromCsv(fileToCheck);
            vegetableMap.forEach((name, vegetable) -> {
                if (VegetableName.UNKNOWN.name().equalsIgnoreCase(name)) {
                    errorList.add("Error in file : " + fileToCheck +
                            " a \"Name\" is Empty or unknown. To correct it, check the authorized value for the \"name\" column in the readme.\n" +
                            "The wrong line is : " + vegetable);
                }
                if (VegetableCategory.UNKNOWN.name().equalsIgnoreCase(vegetable.getCategory())) {
                    errorList.add("Error in file : " + fileToCheck + " the entry : " + name +
                            " has an empty or unknown \"category\". To correct it, check the authorized value for the \"category\" column in the readme.");
                }
                if (VegetableSize.UNKNOWN.name().equalsIgnoreCase(vegetable.getSize())) {
                    errorList.add("Error in file : " + fileToCheck + " the entry : " + name +
                            " has an empty or unknown \"size\". To correct it, check the authorized value for the \"size\" column in the readme.");
                }

                boolean errorInCloseFrom = false;
                for (String closeFromVegetable : vegetable.getCloseFrom()) {
                    if (VegetableName.UNKNOWN.name().equalsIgnoreCase(closeFromVegetable)) {
                        errorInCloseFrom = true;
                    }
                }
                if (errorInCloseFrom) {
                    errorList.add("Error in file : " + fileToCheck + " the entry : " + name +
                            " has at list one empty or unknown name in the \"close from\" column. To correct it, check the authorized value for the \"close from\" column in the readme.");
                }

                boolean errorInFarFrom = false;
                for (String farFromVegetable : vegetable.getFarFrom()) {
                    if (VegetableName.UNKNOWN.name().equalsIgnoreCase(farFromVegetable)) {
                        errorInFarFrom = true;
                    }
                }
                if (errorInFarFrom) {
                    errorList.add("Error in file : " + fileToCheck + " the entry : " + name +
                            " has at list one empty or unknown name in the \"far from\" column. To correct it, check the authorized value for the \"far from\" column in the readme.");
                }

                boolean errorInPlantAfter = false;
                for (String plantAfterVegetable : vegetable.getPlantAfter()) {
                    if (VegetableName.UNKNOWN.name().equalsIgnoreCase(plantAfterVegetable)) {
                        errorInPlantAfter = true;
                    }
                }
                if (errorInPlantAfter) {
                    errorList.add("Error in file : " + fileToCheck + " the entry : " + name +
                            " has at list one empty or unknown name in the \"plant after\" column. To correct it, check the authorized value for the \"plant after\" column in the readme.");
                }
            });
        }
        return errorList;
    }

}
