package com.lite;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Controller {
	
	@GetMapping
	public String get() {
		return "hola equipo del curso del sabado";
	}

}
