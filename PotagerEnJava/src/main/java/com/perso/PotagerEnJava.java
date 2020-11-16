package com.perso;

import com.perso.config.CsvHeaderProperties;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.core.env.Environment;

import java.net.InetAddress;
import java.net.UnknownHostException;

@EnableConfigurationProperties({CsvHeaderProperties.class})
@SpringBootApplication
public class PotagerEnJava {

    private static final Logger logger = LoggerFactory.getLogger(PotagerEnJava.class);

    /**
     * Empty constructor.
     */
    protected PotagerEnJava() {
    }

    /**
     * Main of the SpringBootApplication.
     * Used only to start the server.
     *
     * @param args from run.sh
     * @throws UnknownHostException exception thrown if no InetAddress.getLocalHost().
     */
    public static void main(String[] args) throws UnknownHostException {
        SpringApplication springApplication = new SpringApplicationBuilder(PotagerEnJava.class).build(args);
        ConfigurableApplicationContext context = springApplication.run(args);
        Environment env = context.getEnvironment();
        String protocol = "http";
        if (env.getProperty("server.ssl.key-store") != null) {
            protocol = "https";
        }
        logger.info("\n------------------------------------------------------\n\t"
                        + "Application '{}' is now running! access URLs : \n\t"
                        + "Local: \t\t{}://localhost:{}\n\t"
                        + "External: \t\t{}://{}:{}\n\t" +
                        "------------------------------------------------------",
                env.getProperty("spring.application.name"),
                protocol,
                env.getProperty("server.port"),
                protocol,
                InetAddress.getLocalHost().getHostAddress(),
                env.getProperty("server.port"));

    }

}
