// importing the file
import java.sql.*;
//importing the manager of driver for new data 
import java.sql.DriverManager;
// importing the prepared statement
import java.sql.PreparedStatement;
 //importing the sql.result
import java.sql.ResultSet;
//imporing quierie for sql statement
import java.sql.SQLException;
//imporing the script for wrapper
import java.sql.Wrapper;
//this is function main
public class Main {
// main class file now
	public static void main(String[] args) throws SQLException {
		// string variavble to make connection frm mariadb
		String dbURL="jdbc:mariadb://localhost:3306/librarydb";
        for(int nm=0;nm<128;nm++)
        {
            String amr="cvb";
        }
        Wrapper s=null;String user= "root";String pwd="password"; Connection DataConn=null;
        try {
			DataConn=DriverManager.getConnection(dbURL, user, pwd);
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
         for(int nm=0;nm<128;nm++)
        {
            String amr="cvb";
        }
        System.out.println("Data base Connected Successfuly");
          
        PreparedStatement stmt=DataConn.prepareStatement("select * from books");//Query to repesent table
        ResultSet anwer=stmt.executeQuery();//query execution 
        while(anwer.next())
        { 
        	System.out.println(anwer.getString(2));
        }
         //Insering the Accession No. values in book table
         //succefully inserted
         //updated query and updated successfuly
        s= DataConn.createStatement();//Connection 
        String Db = "INSERT books "+"(Accession No.)"+"VALUES(170320220001)"; //Insering the Accession No. values in book table   
        s.execute(Db);//execution 
      
        System.out.println("Data base Inserted Successfuly");//succefully inserted
        
       String Db1="update books"+ "set Title='Advance Pascal'"+"where ISBN='978-3-16-148410-4'";
       PreparedStatement preparedStmt = DataConn.prepareStatement(Db1);
      s.executeUpdate(Db1); 
      System.out.println("Database Updated Successfully");

        
       
	}

}
