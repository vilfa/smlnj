Name:           smlnj
Version:        %(cat config/version)
Release:        1%{?dist}
Summary:        Standard ML of New Jersey

License:        BSD-3-Clause
URL:            https://www.smlnj.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  git gcc gcc-c++ cmake rpmdevtools

%description
Standard ML of New Jersey (abbreviated SML/NJ) is a compiler for the Standard ML '97 
programming language with associated libraries, tools, and documentation. SML/NJ is 
free, open source software.


%prep
%autosetup


%build
curl -O https://smlnj.org/dist/working/%{Version}/boot.amd64-unix.tgz
./build.sh -doc -verbose -debug


%install
# %make_install


%files
%license LICENSE
# %doc add-docs-here



%changelog
* Mon Oct 24 2022 Luka Vilfan <luka.vilfan@protonmail.com>
- Add COPR build spec.
