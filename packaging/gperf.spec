
Name:       gperf
Summary:    A perfect hash function generator
Version:    3.0.4
Release:    %{?release_prefix:%{release_prefix}.}1.41.%{?dist}%{!?dist:tizen}
VCS:        external/gperf#submit/trunk/20121019.110628-0-g4bf8661a0ed399329a29e18fa40f9e36d4a9336e
Group:      Development/Tools
License:    GPLv2+
URL:        http://www.gnu.org/software/gperf/
Source0:    ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz


%description
GNU gperf is a perfect hash function generator. For a given list of strings, it
produces a hash function and hash table, in form of C or C++ code, for looking
up a value depending on the input string. The hash function is perfect, which 
means that the hash table has no collisions, and the hash table lookup needs 
a single string comparison only. 




%prep
%setup -q -n %{name}-%{version}


%build

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm -f %{buildroot}%{_datadir}/doc/gperf.html






%files
%defattr(-,root,root,-)
%doc NEWS README doc/gperf.html
%doc %{_mandir}/man1/gperf.1*
%doc %{_infodir}/gperf.info*
%{_bindir}/%{name}


%changelog
* Mon Sep 16 2013 UkJung Kim <ujkim@samsung.com> - submit/trunk/20121019.110628 
- PROJECT: external/gperf
- COMMIT_ID: 4bf8661a0ed399329a29e18fa40f9e36d4a9336e
- PATCHSET_REVISION: 4bf8661a0ed399329a29e18fa40f9e36d4a9336e
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/103453
- PATCHSET_REVISION: 4bf8661a0ed399329a29e18fa40f9e36d4a9336e
- TAGGER: UkJung Kim <ujkim@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code Review : 2
- CHANGE_SUBJECT: Initial commit
- [Version] 3.0.4
- [Project] GT-I8800
- [Title] Initial commit
- [BinType] PDA
- [Customer] Open
- [Issue#] N/A
- [Problem] N/A
- [Cause] N/A
- [Solution]
- [Team] SCM
- [Developer] UkJung Kim <ujkim@samsung.com>
- [Request] N/A
- [Horizontal expansion] N/A
- [SCMRequest] N/A
* Sun Feb 21 2010 Anas Nashif <anas.nashif@intel.com> - 3.0.4
- Clean up spec, add description
* Mon Feb  1 2010 Zhang, Qiang Z<qiang.z.zhang@intel.com> 3.0.4
- Switch to spectacle building
* Fri Feb 20 2009 Zhang, Qiang Z<qiang.z.zhang@intel.com> 3.0.4
- Update to 3.0.4
* Tue Dec 16 2008 Anas Nashif <anas.nashif@intel.com> 3.0.3
- fixed spec-builder output
* Tue Dec 16 2008 Anas Nashif <anas.nashif@intel.com> 3.0.3
- Update spec file using latest spec-builder
* Mon Dec  8 2008 Rusty Lynch <rusty.lynch@intel.com> - 1.1.3-1
- Creating a 1.1.3-1 release
