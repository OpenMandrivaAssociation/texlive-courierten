Name:		texlive-courierten
Version:	55436
Release:	2
Summary:	Courier 10 Pitch BT with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/courierten
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courierten.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courierten.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is the font Courier 10 Pitch BT, with LaTeX support and an
OpenType conversion as well.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/courierten
%{_texmfdistdir}/fonts/vf/public/courierten
%{_texmfdistdir}/fonts/type1/public/courierten
%{_texmfdistdir}/fonts/tfm/public/courierten
%{_texmfdistdir}/fonts/opentype/public/courierten
%{_texmfdistdir}/fonts/map/dvips/courierten
%{_texmfdistdir}/fonts/enc/dvips/courierten
%doc %{_texmfdistdir}/doc/fonts/courierten

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
