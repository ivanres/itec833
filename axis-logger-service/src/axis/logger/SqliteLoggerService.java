package axis.logger;
import java.sql.*;

/**
 * Service Entry Point
 * @author Ivan Rodriguez Asqui
 *
 */
public class SqliteLoggerService {

	public int addLog(String cc_number, String cc_type){
		try {
			
			//Inserts the log
			Class.forName("org.sqlite.JDBC");
			Connection conn = DriverManager.getConnection("jdbc:sqlite:C:\\databases\\logs.db");
			String sql = "INSERT INTO logs (cc_number, cc_type) VALUES (?, ?)"; 
			PreparedStatement stat = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
			stat.setString(1, cc_number);
			stat.setString(2, cc_type);
			stat.executeUpdate();
			
			//Get the inserted id
			ResultSet keys = stat.getGeneratedKeys();
			if(keys.next()){
				return keys.getInt(1);
			}
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return -1;
	}
}
