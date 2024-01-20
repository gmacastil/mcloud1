package com.lite;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Controller {
	
	@Value("${env}")
	private String env;
	
	@Value("${host}")
	private String host;
	
	
	@GetMapping
	public String get() {
		return env + ":" + host;
	}

}
