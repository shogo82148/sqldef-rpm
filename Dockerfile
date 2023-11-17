FROM centos:7
ENV HOME /
RUN yum update -y
RUN yum install -y rpm-build redhat-rpm-config rpmdevtools

ARG VERSION
ARG GOARCH
ARG PLATFORM

RUN rpmdev-setuptree
ADD ./rpmbuild/ /rpmbuild/
RUN chown -R root:root /rpmbuild
RUN cd /rpmbuild/SOURCES/ && \
    curl -sSL -O "https://github.com/sqldef/sqldef/releases/download/v${VERSION}/mssqldef_linux_${GOARCH}.tar.gz" && \
    curl -sSL -O "https://github.com/sqldef/sqldef/releases/download/v${VERSION}/mysqldef_linux_${GOARCH}.tar.gz" && \
    curl -sSL -O "https://github.com/sqldef/sqldef/releases/download/v${VERSION}/psqldef_linux_${GOARCH}.tar.gz" && \
    curl -sSL -O "https://github.com/sqldef/sqldef/releases/download/v${VERSION}/sqlite3def_linux_${GOARCH}.tar.gz"
RUN rpmbuild -ba --target "$PLATFORM" /rpmbuild/SPECS/sqldef.spec
RUN tar -czf /tmp/sqldef.tar.gz -C /rpmbuild RPMS SRPMS
CMD ["/bin/true"]
