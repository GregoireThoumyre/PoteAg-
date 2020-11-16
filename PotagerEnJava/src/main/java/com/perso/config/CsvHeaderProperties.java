package com.perso.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;

@Data
@ConfigurationProperties (prefix = "csv")
public class CsvHeaderProperties {
    private String location;
    private String separator;
    private Boolean header;
}
