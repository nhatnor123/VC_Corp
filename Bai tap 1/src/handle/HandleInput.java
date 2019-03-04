package handle;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;

public class HandleInput {

	public void HanleUrl(URL newURL) throws IOException {
		// URL url = new URL("https://www.google.com");

		HttpURLConnection connection = (HttpURLConnection) newURL.openConnection();
		connection.setRequestMethod("GET");
		connection.connect();

		int code = connection.getResponseCode();

		System.out.println(code);

//		switch (code / 100) {
//		case 1:
//			System.out.println("Informational Response");
//			break;
//		case 2:
//			System.out.println("Success");
//			break;
//		case 3:
//			System.out.println("Redirection");
//			break;
//		case 4:
//			System.out.println("Client errors");
//			break;
//		case 5:
//			System.out.println("Server errors");
//			break;
//		default:
//			break;
//		}
	}
}