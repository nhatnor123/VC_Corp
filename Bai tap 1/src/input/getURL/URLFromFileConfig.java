package input.getURL;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class URLFromFileConfig {

	public ArrayList<String> readURL(String dictListURL) throws IOException { //// dictListURL =
																				//// "/home/nhatnor123/Desktop/listURL"
		ArrayList<String> listURL = new ArrayList<String>();

		BufferedReader inputStream = new BufferedReader(new FileReader(new File(dictListURL)));
		try {
			while (inputStream.ready()) {
				listURL.add(inputStream.readLine());
			}
		} finally {
			if (inputStream != null) {
				inputStream.close();
			}
		}
		return listURL;
	}

}
