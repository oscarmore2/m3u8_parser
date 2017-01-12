import java.lang.*;
import java.io.*;

public class ExecuteCommand
{
	String DoExecute(String arg)
	{
		String Result = "";
		Process process = null;
		DataOptputStream DataOS = null;
		try{
			process  = Runtime.getRuntime().exec(arg);
			Result = new BufferedReader(new InputStreamReader(process.getInputStream())).readLine();
		}catch (Exception e)
		{
			e.printStackTrace();
		}
		return Result;
	}

	public String GetYinyuetai(String url)
	{
		return DoExecute("python Yinyetai-m3u8.py"+" "+url);
	}

	public String GetYouku(String url)
	{
		return DoExecute("python Youku-m3u8.py"+" "+url);
	}

	public String GetTudou(String url)
	{
		return DoExecute("python Tudou-m3u8.py"+" "+url);
	}

	public void main()
	{

	}
}
