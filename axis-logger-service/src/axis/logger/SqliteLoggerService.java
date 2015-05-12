package axis.logger;
import java.sql.*;
//import org.sql.*;

public class SqliteLoggerService {

	public int addLog(String cc_number, String cc_type){
		try {
			Class.forName("org.sqlite.JDBC");
			Connection conn = DriverManager.getConnection("jdbc:sqlite:C:\\databases\\logs.db");
			String sql = "INSERT INTO logs (cc_number, cc_type) VALUES (?, ?)"; 
			PreparedStatement stat = conn.prepareStatement(sql);
			stat.setString(1, cc_number);
			stat.setString(2, cc_type);
			stat.execute();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return 79;
	}
}
