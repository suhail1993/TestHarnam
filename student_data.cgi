#!"D:\xampp\perl\bin\perl.exe"

print "Content-Type: text/html\n\n";

use DBI;
use CGI;
use CGI::Carp qw ( fatalsToBrowser );
use strict;

my $form = CGI->new;
my $email = $form->param('email');
my $passwd =$form->param('passwd');

my $driver = "mysql"; 
my $database = "mysql";
my $dsn = "dbi:$driver:database=$database";
my $userid = "root";
my $password = "";


my $dbh = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr;

my $sql = "select marks from student_register where email=$email and password=$passwd";
my $sth = $dbh->prepare($sql);
$sth->execute or die "SQL Error: $DBI::errstr\n";
my @row = $sth->fetchrow_row;

if ( !@row ){
   print"Student not registered yet";
   print qq~<form><input type="button" value="Go Back!" onclick="history.back()"> </form>~;

}else {

    print qq~ <table>
                <tr>
		    	   <td> Name </td> <td> Marks Obtained </td></tr>
                <tr> 
			       <td>$row[0]</td> <td>$row[1]</td>
	 	        </tr>
				</table>~;
 }             
print"$email===$passwd";