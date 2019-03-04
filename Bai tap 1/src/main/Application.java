package main;

import java.io.IOException;
import java.net.URL;
import java.time.LocalDateTime;
import java.util.ArrayList;

import handle.HandleInput;
import input.getURL.URLFromFileConfig;


public class Application {
	public static void main(String[] args) throws IOException {
		HandleInput inputHandle = new HandleInput();

		URLFromFileConfig urlFileConfig = new URLFromFileConfig();

		ArrayList<String> listURL = urlFileConfig.readURL("/home/nhatnor123/Desktop/listURL");

		for (String link : listURL) {
			
			System.out.println("\n" + link);
			inputHandle.HanleUrl(new URL(link));
			System.out.println(LocalDateTime.now());
			
		}
	}
}

