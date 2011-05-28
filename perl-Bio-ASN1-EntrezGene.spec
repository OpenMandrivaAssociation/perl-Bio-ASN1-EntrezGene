%define upstream_name	 Bio-ASN1-EntrezGene
%define upstream_version 1.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Regular expression-based Perl Parser for NCBI Entrez Gene
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Bio/%{upstream_name}-%{upstream_version}-withoutworldwriteables.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Bio::ASN1::EntrezGene is a regular expression-based Perl Parser for NCBI Entrez
Gene genome databases (http://www.ncbi.nih.gov/entrez/query.fcgi?db=gene). It
parses an ASN.1-formatted Entrez Gene record and returns a data structure that
contains all data items from the gene record.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
