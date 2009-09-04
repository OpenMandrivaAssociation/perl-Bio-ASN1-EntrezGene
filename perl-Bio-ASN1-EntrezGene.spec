%define module	Bio-ASN1-EntrezGene
%define name	perl-%{module}
%define version 1.091
%define release %mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Regular expression-based Perl Parser for NCBI Entrez Gene
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Bio/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Bio::ASN1::EntrezGene is a regular expression-based Perl Parser for NCBI Entrez
Gene genome databases (http://www.ncbi.nih.gov/entrez/query.fcgi?db=gene). It
parses an ASN.1-formatted Entrez Gene record and returns a data structure that
contains all data items from the gene record.

%prep
%setup -q -n %{module}-1.09

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
# disabled to avoid bioperl circular dependency
#%{__make} test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Bio
%{_mandir}/*/*



