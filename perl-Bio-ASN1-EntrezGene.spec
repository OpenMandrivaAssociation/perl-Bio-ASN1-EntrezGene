%define upstream_name	 Bio-ASN1-EntrezGene
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Regular expression-based Perl Parser for NCBI Entrez Gene
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Bio/%{upstream_name}-%{upstream_version}-withoutworldwriteables.tar.gz

BuildRequires:	perl-devel

BuildArch:	noarch

%description
Bio::ASN1::EntrezGene is a regular expression-based Perl Parser for NCBI Entrez
Gene genome databases (http://www.ncbi.nih.gov/entrez/query.fcgi?db=gene). It
parses an ASN.1-formatted Entrez Gene record and returns a data structure that
contains all data items from the gene record.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
# disabled to avoid bioperl circular dependency
#%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/Bio
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.100.0-2mdv2011.0
+ Revision: 680658
- mass rebuild

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 552259
- update to

* Fri Feb 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.91.0-1mdv2010.1
+ Revision: 504595
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.091-7mdv2010.0
+ Revision: 430266
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.091-6mdv2009.0
+ Revision: 255432
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.091-4mdv2008.1
+ Revision: 133629
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.091-3mdv2007.0
+ Revision: 73338
- import perl-Bio-ASN1-EntrezGene-1.091-3mdv2007.0

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.091-3mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.091-2mdk
- Fix SPEC Using perl Policies
	- Source URL

* Mon Mar 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.091-1mdk
- first mdk release

