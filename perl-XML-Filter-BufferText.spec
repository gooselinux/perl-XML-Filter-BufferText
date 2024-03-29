Name:           perl-XML-Filter-BufferText
Version:        1.01
Release:        8%{?dist}
Summary:        Filter to put all characters() in one event
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-Filter-BufferText/
Source0:        http://www.cpan.org/modules/by-module/XML/XML-Filter-BufferText-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::Base), perl(ExtUtils::MakeMaker), perl(Test::More)

%description
This is a very simple filter. One common cause of grief (and programmer
error) is that XML parsers aren't required to provide character events in
one chunk. They can, but are not forced to, and most don't. This filter
does the trivial but oft-repeated task of putting all characters into a
single event.

%prep
%setup -q -n XML-Filter-BufferText-%{version}
chmod 644 Changes README BufferText.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.01-8
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-5
- Rebuild for perl 5.10 (again)

* Tue Jan 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.01-4
- BR perl(Test::More)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.01-3
- rebuild for new perl

* Sat Mar 17 2007 Andreas Thienemann <andreas@bawue.net> 1.01-2
- Fixed dependencies

* Thu Mar 15 2007 Andreas Thienemann <andreas@bawue.net> 1.01-1
- Specfile autogenerated by cpanspec 1.69.1.
- Cleaned up for FE
