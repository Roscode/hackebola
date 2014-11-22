#!/usr/bin/perl 

use warnings;
use strict;
use diagnostics;
use feature qw(say);

#####################
#
#   Copyright © Andres Breton
#   File: columnator.pl
#
#   Extract desired column pairs for comparison or other IO uses
#
#####################


##########################
# VARIABLES

my $inFile = $ARGV[0];
my $outFile;
my $outputFileName = "columnator_out.csv";  #Change desired output file

my $column1 = 8;    #Change to desired column pairs
my $column2 = 18;   #Remember to start count at 0

my ($col1, $col2) = columnPairs($column1, $column2);
my @col1 = @$col1;
my @col2 = @$col2;

my $col1Size = @col1;   #Number of data points extracted
my $col2Size = @col2;


##########################
# CHECKS

if(! $inFile) {
    die "You did not provide an input file", $!;
}


##########################
# USER INPUT

say "\n$col1Size number of data points extracted";

my $response = "none";

until ($response eq "view" || $response eq "file") {
    print "\nWould you like to view or create file with data? ";
    my $response = lc <STDIN>;
    chomp $response;
    
    if ($response eq "view") {
        for (my $i = 0; $i < $col1Size; $i++) {
            say "$col1[$i]    $col2[$i]";
        }
        exit;
    }elsif ($response eq "file") {
        $outFile = $outputFileName;
        
        unless(open(OUTFILE, ">", $outFile)){
            die "Can not open output file $outFile for writing", "\n", $!;
        }
        
        for (my $i = 0; $i < $col1Size; $i++) {
            say OUTFILE "$col1[$i]\t$col2[$i]";
        }
        close OUTFILE;
        say "File $outputFileName created successfully";
        exit;
    }else {
        say "Please provide answer as \"view\" or \"file\"";
    }
}

##########################
# SUB

sub columnPairs {
    my ($column1, $column2)= @_;
    
    unless (open(INFILE, "<", $inFile)) {
        die "Can not open input file $inFile", $!;
    }
    
    for (<INFILE>) {
        chomp;
        my @line = split /\t/;
        my $tempCol1 = $line[$column1];
        my $tempCol2 = $line[$column2];
        push @col1, $tempCol1;
        push @col2, $tempCol2;
    }
    return \@col1, \@col2;
    close INFILE;
}


