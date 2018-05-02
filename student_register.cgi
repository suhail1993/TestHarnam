#!"D:\xampp\perl\bin\perl.exe"

print "Content-Type: text/html\n\n";

use CGI;
use DBI;
use CGI::Carp qw ( fatalsToBrowser );
use strict;
use CAM::PDF;

my $mark_file_dir="D:\suhail";

my $form = CGI->new;
my $marks_file = $form->param('marks');
if ( !$marks_file ) {
   print $form->header();
   print "There was a problem uploading marks file ";
   exit;
}

my ( $file, $path, $ext ) = fileparse ( $marks_file, '..*' );
$mark_file = $file . $ext;

$mark_file =~ tr/\s+/_/;

my $upload_file = $form->upload('marks');

open(UPLOAD, ">$mark_file_dir/$mark_file" ) or die "$!\n"; binmode UPLOAD;

while (<$upload_file>) {
    print UPLOAD;
}

close(UPLOAD);

my $name = $form->param('name');
my $city =$form->param('city');
my $dd =$form->param('dd');
my $mm =$form->param('mm');
my $yy =$form->param('yy');
my $dob="$dd-$mm-$yy";
my $street1 =$form->param('strt1');
my $street2 =$form->param('strt2');
my $street3 =$form->param('strt3');
my $contact =$form->param('contact');
my $state =$form->param('state');
my $country =$form->param('country');
my $pin_code =$form->param('pin');
my $email =$form->param('email');
my $password =$form->param('pass');
my $marks =$form->param('marks');

my $driver = "mysql"; 
my $database = "mysql";
my $dsn = "dbi:$driver:database=$database";
my $userid = "root";
my $password = "";

my $pdf= CAM::PDF->new($pdf_file);
for my $text (1..$pdf->$pdf_file) {
  my $marks_data = $pdf->getPageText($text);
  my $marks = join("|", split(/\n/,$marks_data));
}

my $dbh = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr;

my $sth = $dbh->prepare("INSERT INTO student_register
                            (name, city, dob, street1, street2, street3, contact, state, pin, country, email, password, marks )
                          values
                            ($name, $city, $dd, $mm,$yy, $dob,$street1,$street2,$street3,$contact,$state,$country,$pin_code,$email,$password,$marks)
					   ");
$sth->execute() or die $DBI::errstr;
$sth->finish();


print" Student Data uploaded successfully";