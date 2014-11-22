#!/usr/bin/perl 

use warnings;
use strict;
use diagnostics;
use feature qw(say);
#use Chart::Clicker;

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
my $arguments = @ARGV;
my $outFile;
my $outputFileName = "_out.csv";

my $column1 = 2;    #Change to desired column pairs
my $column2 = 8;    #Remember to start count at 0
my $column3 = 18;

my ($col1, $col2, $col3) = columnPairs($column1, $column2, $column3);
my @col1 = @$col1;
my @col2 = @$col2;
my @col3 = @$col3;

my $col1Size = @col1;   #Number of data points extracted
my $col2Size = @col2;


##########################
# CHECKS

if(! $inFile) {
    die "You did not provide an input file", $!;
}

if ($arguments > 2) {
    say "You provided too many arguments. Only provide input file OR input file plus out file name if desired";
    say "\nExample: \$ columnator.pl inFile.csv outFile.csv\n";
    exit;
}


##########################
# USER INPUT

say "\n$col1Size number of data points extracted";

my $response = "none";

until ($response eq "view" || $response eq "file") {
    print "\nWould you like to view or create file with data? For file, provide file name desired: ";
    my $response = lc <STDIN>;
    chomp $response;

    if ($response eq "view") {
        for (my $i = 0; $i < $col1Size; $i++) {
            say "$col1[$i]\t$col2[$i]\t$col3[$i]";
        }
        exit;
    }else {
        $outFile = $response."_out.csv";
        
        unless(open(OUTFILE, ">", $outFile)){
            die "Can not open output file $outFile for writing", "\n", $!;
        }
        
        for (my $i = 0; $i < $col1Size; $i++) {
            say OUTFILE "$col1[$i]\t$col2[$i]\t\t$col3[$i]";
        }
        close OUTFILE;
        say "File $outFile created successfully";
        exit;
    }
#   else {
#        say "Please provide answer as \"view\" or \"file\"";
#    }
}

##########################
# SUB

sub columnPairs {
    my ($column1, $column2, $column3)= @_;
    
    unless (open(INFILE, "<", $inFile)) {
        die "Can not open input file $inFile", $!;
    }
    
    for (<INFILE>) {
        chomp;
        my @line = split /\t/;
        my $tempCol1 = $line[$column1];
        my $tempCol2 = $line[$column2];
        my $tempCol3 = $line[$column3];
        push @col1, $tempCol1;
        push @col2, $tempCol2;
        push @col3, $tempCol3;
    }
    close INFILE;
    #graph (\@col1, \@col2, \@col3);
    return \@col1, \@col2, \@col3;

}

sub graph {
    my ($series1, $series2, $series3) = @_;
    my $cc = Chart::Clicker->new;
}


